"""
The websocket client to connect to websocket to recieve realtime feeds.
The WsClient contains decorators to assign handlers for listening to messages.

These decorators include:
  - `on_message(topic)` - Runs on every message
  - `on_connect` - Runs once connection is established (Provides the connection acknowedgement message)
  - `on_close` - Runs once the connection is closed

Example:

```python
from typing import Any
from pyClient.websocket import WsClient
from pyClient import Client, LoginRequestModel, RequestSourceType
import os
from dotenv import load_dotenv

from pyClient.websocket.enums import MessageTopic

load_dotenv()

client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
ws = client.ws

# login
login_model = LoginRequestModel(
  apkversion = os.getenv('APK_VERSION'),
  appkey = os.getenv('APP_KEY'),
  vc = os.getenv('VC'),
  uid = os.getenv('UID'),
  pwd = os.getenv('PASSWORD'),
  factor2 = os.getenv("FACTOR2"),
  imei = "134243434",
  source = RequestSourceType.API
)
client.login(login_model)

@ws.on_message(MessageTopic.TOUCHLINE_FEED)
def msg_handler(client: WsClient, message: Any):
  print(message)

@ws.on_connect
def cnc_handler(client: WsClient, message: Any):
  print(message)


ws.connect(os.getenv('UID'), os.getenv('UID'))
ws.subscribe_touchline('NSE', 'NIFTY')
# run forever
ws.run_forever()
```

> Note: It uses ws4py under the hood to connect to websocket
"""
from .client import *
from .models import *
from .enums import *