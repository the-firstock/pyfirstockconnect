# The Firstock Connect API Python client - v3  


To communicate with the Firstock Connect API using Python, you can use the official Python client library provided by Firstock.
<br /> Licensed under the MIT License.

## Documentation 
* python client documentation

## v3 - Changes 
* Error code response structured has been changed
* Renamed

## Installing the client 
You can install the pre release via pip
```bash
 pip install --upgrade thefirstock
```
Its recommended to update setuptools to latest if you are facing any issue while installing
```bash
pip install -U pip setuptools
```
Since some of the dependencies uses C extensions it has to compiled before installing the package.

## API usage 

```python
from thefirstock import thefirstock

login = thefirstock.firstock_login(userId='', password='', TOTP='', vendorCode='', apiKey='')

"""Place an order"""
placeOrder = thefirstock.firstock_placeOrder(
    exchange="",
    tradingSymbol="",
    quantity="",
    price="",
    product="",
    transactionType="",
    priceType="",
    retention="",
    triggerPrice="",
    remarks=""
)

"Fetch single order deatils"
SOH = thefirstock.firstock_SingleOrderHistory(
    orderNumber=placeOrder["data"]["orderNumber"],
)

"""Order book"""
orderBook = thefirstock.firstock_orderBook()

"""Cancel order"""
cancelOrder = thefirstock.firstock_cancelOrder(orderNumber=placeOrder["data"]["orderNumber"])


"""Historical data"""
timePriceSeries = thefirstock.firstock_TimePriceSeries(
    exchange="NSE",
    token="22",
    startTime="16/08/2022 09:45:32",
    endTime="15/02/2023 13:45:32",
    interval="5"
)
```
Refer to the Firstock Connect Documentation for the complete list of supported methods.

## WebSocket usage 
```python
from typing import Any
from thefirstock.firstockModules import firstockWebSockets
from thefirstock.pyClient.websocket import WsClient
from thefirstock.pyClient.websocket.enums import MessageTopic

"""Initializer"""
client = firstockWebSockets.webSocketLogin()
ws = client.ws


@ws.on_connect
def connected(client, message):
    """Establishment of connection for required symbol"""
    if message.get('s') == 'OK':
        client.subscribe_feed('NSE', '26000') # Subscribe to NIFTY
        client.subscribe_feed('NSE', '26009') # Subscribe to BANKNIFTY


@ws.on_message(MessageTopic.SUBSCRIBE_FEED)
def msg_handler(client: WsClient, message: Any):
    """Prints the message successfully"""
    print(message)


ws.connect(uid='userId', actid='userId')
ws.run_forever()
```

## Run unit tests
```bash
python setup.py test
```
## Changelog
Check release notes.







