"""
The pyClient library abstracts away the REST communication logic by exposing a set of classes and
methods to effectively execute the tasks.

Library exposes a **Client** which abstracts the underlying logic by providing methods and submodules
to communicate with the server.

```py
from pyClient import Client, LoginRequestModel, HttpException

client = Client(api_url=API_URL, socket_url=SOCKET_URL)

login_model = LoginRequestModel(...)

try:
  response = client.login(login_model)
  print('Success')
  print(response.json(exclude_unset=True))
except HttpException as e:
  print('Failed: ', e.reason)
except:
  print('Connection failed')
```

The library uses **requests** library under the hood to interface with the REST API.

.. include:: ./documentation.md
"""
__version__ = '0.1.0'

__all__ = [
    'Client', 'WsClient',
    'AlertsDataSource', 'FundsDataSource', 'MarketsDataSource',
    'OrdersDataSource', 'UserDataSource', 'WatchListDataSource'
  ]

from .common import *
from .websocket import *
from .client import *
