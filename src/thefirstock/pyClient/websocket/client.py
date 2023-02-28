"""
The websocket client
"""

from typing import Any, Callable, Dict
import json
from ws4py.client.threadedclient import WebSocketClient
from ws4py.messaging import TextMessage
from collections import defaultdict

from thefirstock.pyClient.websocket.models.order import OrderSubscribeModel, OrderUnsubscribeModel

from ..utils.stateful import Stateful
from .models import *

__all__ = ['WsClient']


class WsClient(WebSocketClient, Stateful):
    """
  The websocket client for realtime data
  """

    def __init__(self, url: str, state: Dict[str, Any] = {}):
        """
    Initialize the websocket client

    Args:
        url (str): The socket url
        state (Dict[str, Any], optional): The shared state from main client. Defaults to {}.
    """
        super().__init__(url)
        self.__state__ = state
        # the listeners
        self.__connection_model = None
        self.__on_connect_handlers = []
        self.__on_close_handlers = []
        self.__on_message_handlers: Dict[MessageTopic, Callable] = defaultdict(lambda: [])

    def on_connect(self, handler: Callable[['WsClient', Dict[str, Any]], None]):
        """
    Add on open handler

    Args:
      handler (Callable[[WsClient, Dict[str, Any]], None]): The handler to run on connection opened

    Usage:
      Should be used as decorator
      ```python
      @ws.on_connect
      def on_connect(client, ack: Dict[str, Any]):
        print('Connected: ', ack)
      ```
    """
        self.__on_connect_handlers.append(handler)

    def on_close(self, handler: Callable[['WsClient'], None]):
        """
    Add on close handler

    Args:
      handler (Callable[[WsClient], None]): The handler to run on connection closed

    Usage:
      Should be used as decorator
      ```python
      @ws.on_close
      def on_close(client):
        print('Connection closed')
      ```
    """
        self.__on_close_handlers.append(handler)

    def on_message(self, topic: MessageTopic):
        """
    Add on close handler

    Args:
      topic (MessageTopic): The handler to run when a new message is recieved

    Returns:
      Callable[[Callable[['WsClient', Dict[str, Any]], None]], None]

    Usage:
      Should be used as decorator
      ```python
      @ws.on_message(MessageTopic.DEPTH_FEED)
      def on_depth_feed(client, message: Dict[str, Any]):
        print(message)
      ```
    """

        def register(handler: Callable[['WsClient', Dict[str, Any]], None]):
            self.__on_message_handlers[topic].append(handler)

        return register

    def connect(self, uid: str, actid: str):
        """
    Connect to websocket

    Args:
        uid (str): The user id for the user
        actid (str): The account id for the user
    """
        model = WebsocketConnectionModel(
            uid=uid,
            actid=actid,
            susertoken=self.get_state('token')
        )
        self.__connection_model = model
        return super().connect()

    def subscribe_feed(self, *scriplists: List[str]):
        """
    Subscribe to touchline feed

    Args:
      scriplists (List[str]): One or more scriplists
    """
        model = TouchlineSubscribeModel(k=scriplists)
        self.send(model.json())

    def unsubscribe_feed(self, *scriplists: List[str]):
        """
    Unsubscribe from touchline feed

    Args:
      scriplists (List[str]): One or more scriplists
    """
        model = TouchlineUnsubscribeModel(k=scriplists)
        self.send(model.json())

    def subscribe_depth(self, *scriplists: List[str]):
        """
    Subscribe to depth feed

    Args:
      scriplists (List[str]): One or more scriplists
    """
        model = DepthSubscribeModel(k=scriplists)
        self.send(model.json())

    def unsubscribe_depth(self, *scriplists: List[str]):
        """
    Unsubscribe from depth feed

    Args:
      scriplists (List[str]): One or more scriplists
    """
        model = DepthUnsubscribeModel(k=scriplists)
        self.send(model.json())

    def subscribe_order(self, actid: str):
        """
    Subscribe to depth feed

    Args:
      actid (str): Account id based on which order updated to be sent.
    """
        model = OrderSubscribeModel(actid=actid)
        self.send(model.json())

    def unsubscribe_order(self, actid: str):
        """
    Unsubscribe from depth feed

    Args:
      actid (str): Account id based on which order updated to be sent.
    """
        model = OrderUnsubscribeModel(actid=actid)
        self.send(model.json())

    def opened(self):
        """
    This method runs once the connection is established
    ..warning:: Do not call this method directly
    """
        if self.__connection_model is not None:
            self.send(self.__connection_model.json())

    def closed(self):
        """
    This method runs once the connection is closed.
    ..warning:: Do not call this method directly
    """
        for handler in self.__on_close_handlers:
            handler(self)

    def received_message(self, message: TextMessage):
        """
    This method runs for every message
    ..warning:: Do not call this method directly
    """
        message = json.loads(message.data)
        if message['t'] == MessageTopic.CONNECTION_ACK:
            for handler in self.__on_connect_handlers:
                handler(self, message)
            for handler in self.__on_message_handlers[MessageTopic.CONNECTION_ACK]:
                handler(self, message)
        else:
            for handler in self.__on_message_handlers[message['t']]:
                handler(self, message)
