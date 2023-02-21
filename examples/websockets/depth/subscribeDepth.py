from typing import Any
from thefirstock.firstockModules import firstockWebSockets
from thefirstock.pyClient.websocket import WsClient
from thefirstock.pyClient.websocket.enums import MessageTopic


client = firstockWebSockets.webSocketLogin()
ws = client.ws


@ws.on_connect
def connected(client, message):
    if message.get('s') == 'OK':
        client.subscribe_depth('NSE', "22")


@ws.on_message(MessageTopic.DEPTH_FEED)
def msg_handler(client: WsClient, message: Any):
    print(message)


ws.connect(uid='userId', actid='userId')
ws.run_forever()
