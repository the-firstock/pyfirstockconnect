from thefirstock.lookUpTable.lookUpTableCreation import *


MAX_SIZE = 100
symbol_subscribe_queue = Queue(maxsize=MAX_SIZE)
symbol_subscribe_depth_queue = Queue()
symbol_unsubscribe_queue = Queue()
symbol_unsubscribe_depth_queue = Queue()
subscribed_symbols = set()


async def handle_symbol_subscriptions_and_unsubscriptions_feed(websocket, userId, activate_sub_feed, activate_depth_feed):
    """
    Continuously checks for new symbols in the queue and subscribes to them.

    Args:
        websocket: The active WebSocket connection.
        userId: User identifier for the subscription request.
    """
    while True:
        if activate_sub_feed:
            if not symbol_subscribe_queue.empty():
                new_symbol = symbol_subscribe_queue.get()
                if new_symbol not in subscribed_symbols:
                    sym_data = match_data(new_symbol, main())
                    if sym_data:
                        subscription_request = {
                            "t": "t",
                            "k": f'{sym_data["Exchange"]}|{sym_data["Token"]}',
                            "actid": userId
                        }
                        subscribed_symbols.add(new_symbol)
                        await websocket.send(json.dumps(subscription_request))
                    else:
                        print(f"Symbol {new_symbol} not found in lookup table.")
            await asyncio.sleep(1)

            if not symbol_unsubscribe_queue.empty():
                symbol_to_unsubscribe = symbol_unsubscribe_queue.get()
                if symbol_to_unsubscribe in subscribed_symbols:
                    sym_data = match_data(symbol_to_unsubscribe, main())
                    if sym_data:
                        unsubscription_request = {
                            "t": "u",
                            "k": f'{sym_data["Exchange"]}|{sym_data["Token"]}',
                            "actid": userId
                        }
                        subscribed_symbols.remove(symbol_to_unsubscribe)
                        await websocket.send(json.dumps(unsubscription_request))
            await asyncio.sleep(1)

        if activate_depth_feed:
            if not symbol_subscribe_depth_queue.empty():
                new_symbol = symbol_subscribe_depth_queue.get()
                if new_symbol not in subscribed_symbols:
                    sym_data = match_data(new_symbol, main())
                    if sym_data:
                        subscription_request = {
                            "t": "d",
                            "k": f'{sym_data["Exchange"]}|{sym_data["Token"]}',
                            "actid": userId
                        }
                        subscribed_symbols.add(new_symbol)
                        await websocket.send(json.dumps(subscription_request))
                    else:
                        print(f"Symbol {new_symbol} not found in lookup table.")
            await asyncio.sleep(1)

            if not symbol_unsubscribe_depth_queue.empty():
                symbol_to_unsubscribe = symbol_unsubscribe_depth_queue.get()
                if symbol_to_unsubscribe in subscribed_symbols:
                    sym_data = match_data(symbol_to_unsubscribe, main())
                    if sym_data:
                        unsubscription_request = {
                            "t": "ud",
                            "k": f'{sym_data["Exchange"]}|{sym_data["Token"]}',
                            "actid": userId
                        }
                        subscribed_symbols.remove(symbol_to_unsubscribe)
                        await websocket.send(json.dumps(unsubscription_request))
            await asyncio.sleep(1)


async def send_connection_key_request(userId, websocket):
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)

    connection_key_request = {
        "t": "c",
        "uid": userId,
        "actid": userId,
        "susertoken": config_data[userId]["jKey"],
        "source": "API"
    }

    await websocket.send(json.dumps(connection_key_request))

    response = await websocket.recv()
    dict_response = ast.literal_eval(response)
    if dict_response["s"] == "OK":
        print({"message": "Connection Established"})


def match_data(symbol, lookup_table):
    if symbol in lookup_table:
        return lookup_table[symbol]
    else:
        return None


async def send_continuous_feed_request(userId, websocket, list_of_symbols, callback_sub_feed=None,
                                       activate_sub_feed=False,
                                       callback_order_feed=None, activate_order_feed=False, callback_depth_feed=None,
                                       activate_depth_feed=False):
    sym = main()
    connection_string = ""

    for symbols in list_of_symbols:
        if activate_sub_feed:
            subscribed_symbols.add(symbols)
        elif activate_depth_feed:
            subscribed_symbols.add(symbols)
        result = match_data(symbols, sym)

        if connection_string:
            connection_string = f'{connection_string}#{result["Exchange"]}|{result["Token"]}'
        else:
            connection_string = f'{result["Exchange"]}|{result["Token"]}'

    if activate_sub_feed:
        subscribe_feed = {
            "t": "t",
            "k": connection_string
        }
        await websocket.send(json.dumps(subscribe_feed))

    if activate_order_feed:
        order_feed = {
            "t": "o",
            "actid": userId
        }
        await websocket.send(json.dumps(order_feed))

    if activate_depth_feed:
        depth_feed = {
            "t": "d",
            "k": connection_string
        }
        await websocket.send(json.dumps(depth_feed))

    while True:
        feed_response = await websocket.recv()
        dict_response = ast.literal_eval(feed_response)

        if dict_response["t"] == "tk" or dict_response["t"] == "tf":
            callback_sub_feed(dict_response)

        if dict_response["t"] == "dk" or dict_response["t"] == "df":
            callback_depth_feed(dict_response)

        if dict_response["t"] == "om":
            callback_order_feed(dict_response)


async def connect_and_receive_feed(userId, symbols, socket_connection, callback_sub_feed=None, activate_sub_feed=False,
                                   callback_order_feed=None, activate_order_feed=False, callback_depth_feed=None,
                                   activate_depth_feed=False):
    conn1 = "wss://norenapi.thefirstock.com/NorenWSTP/"
    conn2 = "ws://norenapi.thefirstock.com:5810/NorenWSTP/"

    if socket_connection == 1:
        async with websockets.connect(conn1) as websocket:
            asyncio.create_task(handle_symbol_subscriptions_and_unsubscriptions_feed(websocket, userId,
                                                                                     activate_sub_feed,
                                                                                     activate_depth_feed))
            await send_connection_key_request(userId, websocket)
            await send_continuous_feed_request(userId, websocket, symbols, callback_sub_feed, activate_sub_feed,
                                               callback_order_feed, activate_order_feed, callback_depth_feed,
                                               activate_depth_feed)

    elif socket_connection == 2:
        async with websockets.connect(conn2) as websocket:
            asyncio.create_task(handle_symbol_subscriptions_and_unsubscriptions_feed(websocket, userId))
            await send_connection_key_request(userId, websocket)
            await send_continuous_feed_request(userId, websocket, symbols, callback_sub_feed, activate_sub_feed,
                                               callback_order_feed, activate_order_feed, callback_depth_feed,
                                               activate_depth_feed)


def websocket_connection(userId, sym, socket_connection, callback_sub_feed=None, activate_sub_feed=False,
                         callback_order_feed=None,
                         activate_order_feed=False, callback_depth_feed=None, activate_depth_feed=False):

    if activate_sub_feed is True and callback_sub_feed is None:
        print("callback_sub_feed cannot be None")
    elif activate_sub_feed is True and callback_sub_feed is not None:
        asyncio.get_event_loop().run_until_complete(
            connect_and_receive_feed(userId, sym, socket_connection, callback_sub_feed, activate_sub_feed,
                                     callback_order_feed, activate_order_feed, callback_depth_feed, activate_depth_feed))

    elif activate_depth_feed is True and callback_depth_feed is None:
        print("callback_depth_feed cannot be None")

    elif activate_depth_feed is True and callback_depth_feed is not None:
        asyncio.get_event_loop().run_until_complete(
            connect_and_receive_feed(userId, sym, socket_connection, callback_sub_feed, activate_sub_feed,
                                     callback_order_feed, activate_order_feed, callback_depth_feed,
                                     activate_depth_feed))


def subscribe_symbol(symbol):
    symbol_subscribe_queue.put(symbol)


def unsubscribe_symbol(symbol):
    symbol_unsubscribe_queue.put(symbol)


def subscribe_symbol_depth(symbol):
    symbol_subscribe_depth_queue.put(symbol)


def unsubscribe_symbol_depth(symbol):
    symbol_unsubscribe_depth_queue.put(symbol)
