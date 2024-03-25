from thefirstock.lookUpTable.lookUpTableCreation import *

MAX_SIZE = 100

# Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Function for Matching Data
def match_data(symbol, lookup_table):
    return lookup_table.get(symbol)


# WebSocket Handler Class
class WebSocketHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.config = self.load_config()
        self.symbol_subscribe_queue = Queue(maxsize=MAX_SIZE)
        self.symbol_subscribe_depth_queue = Queue()
        self.symbol_unsubscribe_queue = Queue()
        self.symbol_unsubscribe_depth_queue = Queue()
        self.subscribed_symbols = set()

    @staticmethod
    def load_config():
        try:
            with open('config.json', 'r') as config_file:
                return json.load(config_file)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return None

    async def handle_subscriptions(self, websocket, activate_sub_feed, activate_depth_feed):
        try:
            while True:
                await self.process_subscription_queue(self.symbol_subscribe_queue, websocket, activate_sub_feed, 't')
                await self.process_subscription_queue(self.symbol_unsubscribe_queue, websocket, activate_sub_feed, 'u')
                await self.process_subscription_queue(self.symbol_subscribe_depth_queue, websocket, activate_depth_feed,
                                                      'd')
                await self.process_subscription_queue(self.symbol_unsubscribe_depth_queue, websocket,
                                                      activate_depth_feed, 'ud')
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            logger.info("Subscription handler task cancelled")

    async def process_subscription_queue(self, queue, websocket, activate_feed, feed_type):
        if activate_feed and not queue.empty():
            symbol = queue.get()
            if (feed_type in ['t', 'd'] and symbol not in self.subscribed_symbols) or \
                    (feed_type in ['u', 'ud'] and symbol in self.subscribed_symbols):
                sym_data = match_data(symbol, main())
                if sym_data:
                    request = {
                        "t": feed_type,
                        "k": f'{sym_data["Exchange"]}|{sym_data["Token"]}',
                        "actid": self.user_id
                    }
                    if feed_type in ['t', 'd']:
                        self.subscribed_symbols.add(symbol)
                    elif feed_type in ['u', 'ud']:
                        self.subscribed_symbols.remove(symbol)
                    await websocket.send(json.dumps(request))
                else:
                    logger.warning(f"Symbol {symbol} not found in lookup table.")
            await asyncio.sleep(1)

    async def send_connection_key_request(self, websocket):
        try:
            if not self.config:
                raise ValueError("Configuration not loaded")

            connection_key_request = {
                "t": "c",
                "uid": self.user_id,
                "actid": self.user_id,
                "susertoken": self.config[self.user_id]["jKey"],
                "source": "API"
            }

            await websocket.send(json.dumps(connection_key_request))

            response = await websocket.recv()
            dict_response = ast.literal_eval(response)
            if dict_response["s"] == "OK":
                logger.info({"message": "Connection Established"})
            else:
                logger.error({"message": "Connection Failed", "response": dict_response})
        except Exception as e:
            logger.error(f"Failed to send connection key request: {e}")

    async def send_continuous_feed_request(self, websocket, list_of_symbols, callback_sub_feed=None,
                                           activate_sub_feed=False, callback_order_feed=None,
                                           activate_order_feed=False, callback_depth_feed=None,
                                           activate_depth_feed=False):
        try:
            sym = main()
            connection_string = ""

            for symbol in list_of_symbols:
                if symbol in sym:
                    result = sym[symbol]
                    if connection_string:
                        connection_string += f'#{result["Exchange"]}|{result["Token"]}'
                    else:
                        connection_string = f'{result["Exchange"]}|{result["Token"]}'
                else:
                    logger.warning(f"Symbol {symbol} not found in lookup table")

            if activate_sub_feed:
                subscribe_feed = {"t": "t", "k": connection_string}
                await websocket.send(json.dumps(subscribe_feed))

            if activate_order_feed:
                order_feed = {"t": "o", "actid": self.user_id}
                await websocket.send(json.dumps(order_feed))

            if activate_depth_feed:
                depth_feed = {"t": "d", "k": connection_string}
                await websocket.send(json.dumps(depth_feed))

            while True:
                feed_response = await websocket.recv()
                dict_response = ast.literal_eval(feed_response)

                if dict_response["t"] in ["tk", "tf"] and callback_sub_feed:
                    callback_sub_feed(dict_response)
                elif dict_response["t"] in ["dk", "df"] and callback_depth_feed:
                    callback_depth_feed(dict_response)
                elif dict_response["t"] == "om" and callback_order_feed:
                    callback_order_feed(dict_response)
        except asyncio.CancelledError:
            logger.info("Continuous feed task cancelled")
        except Exception as e:
            logger.error(f"Error in send_continuous_feed_request: {e}")

    async def connect_and_receive_feed(self, symbols, socket_connection, callback_sub_feed=None,
                                       activate_sub_feed=False,
                                       callback_order_feed=None, activate_order_feed=False, callback_depth_feed=None,
                                       activate_depth_feed=False):
        try:
            conn1 = "wss://norenapi.thefirstock.com/NorenWSTP/"
            conn2 = "ws://norenapi.thefirstock.com:5810/NorenWSTP/"
            connection_url = conn1 if socket_connection == 1 else conn2

            async with websockets.connect(connection_url) as websocket:
                subscription_handler = asyncio.create_task(
                    self.handle_subscriptions(websocket, activate_sub_feed, activate_depth_feed))
                await self.send_connection_key_request(websocket)
                await self.send_continuous_feed_request(websocket, symbols, callback_sub_feed, activate_sub_feed,
                                                        callback_order_feed, activate_order_feed, callback_depth_feed,
                                                        activate_depth_feed)
                await subscription_handler
        except Exception as e:
            logger.error(f"Failed to connect and receive feed: {e}")


    async def shutdown(self):
        """ Gracefully shut down the handler. """
        # Cancel ongoing tasks, if any
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        [task.cancel() for task in tasks]

        # Wait for the tasks to be cancelled
        await asyncio.gather(*tasks, return_exceptions=True)


def websocket_connection(handler, sym, socket_connection, callback_sub_feed=None, activate_sub_feed=False,
                         callback_order_feed=None, activate_order_feed=False, callback_depth_feed=None,
                         activate_depth_feed=False, run_in_background=False):
    """
    Establishes a WebSocket connection and initiates feed handling.

    Args:
        userId: User identifier for the WebSocket connection.
        sym: Symbols or data required for the connection.
        socket_connection: Specifies the socket connection type.
        callback_sub_feed: Callback function for subscription feed.
        activate_sub_feed: Flag to activate subscription feed.
        callback_order_feed: Callback function for order feed.
        activate_order_feed: Flag to activate order feed.
        callback_depth_feed: Callback function for depth feed.
        activate_depth_feed: Flag to activate depth feed.
    """
    def run_event_loop():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                handler.connect_and_receive_feed(sym, socket_connection, callback_sub_feed, activate_sub_feed,
                                                 callback_order_feed, activate_order_feed, callback_depth_feed,
                                                 activate_depth_feed))
        finally:
            loop.close()

    if run_in_background:
        thread = threading.Thread(target=run_event_loop)
        thread.start()
        return thread
    else:
        asyncio.run(handler.connect_and_receive_feed(sym, socket_connection, callback_sub_feed, activate_sub_feed,
                                                     callback_order_feed, activate_order_feed, callback_depth_feed,
                                                     activate_depth_feed))


def subscribe_symbol(handler, symbol):
    """
    Enqueues a symbol for subscription if it's not already subscribed.

    Args:
        handler: The WebSocketHandler instance.
        symbol: The symbol to subscribe.
    """
    if symbol not in handler.subscribed_symbols:
        handler.symbol_subscribe_queue.put(symbol)


def unsubscribe_symbol(handler, symbol):
    """
    Enqueues a symbol for unsubscription.

    Args:
        handler: The WebSocketHandler instance.
        symbol: The symbol to unsubscribe.
    """
    handler.symbol_unsubscribe_queue.put(symbol)


def subscribe_symbol_depth(handler, symbol):
    """
    Enqueues a symbol for depth subscription.

    Args:
        handler: The WebSocketHandler instance.
        symbol: The symbol for which depth information is subscribed.
    """
    handler.symbol_subscribe_depth_queue.put(symbol)


def unsubscribe_symbol_depth(handler, symbol):
    """
    Enqueues a symbol for depth unsubscription.

    Args:
        handler: The WebSocketHandler instance.
        symbol: The symbol for which depth information is unsubscribed.
    """
    handler.symbol_unsubscribe_depth_queue.put(symbol)
