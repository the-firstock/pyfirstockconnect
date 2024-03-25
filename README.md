# Firstock Connect API Python Client - v4

The official Python library for the Firstock Connect API, providing a seamless interaction with Firstock's trading and financial data services. This library has been designed for developers to easily integrate Firstock's advanced trading capabilities into their Python applications.

## Features

- HTTP calls are converted to methods.
- JSON responses are wrapped into Python-compatible objects.
- The handling of WebSocket connections is automated.

## Installation
This module is installed via pip:
```python
pip install thefirstock
```

## Getting started with API
The API consists of five major section 
* Login & Profile
* Orders & Report
* Market Connect
* Strategies
* Websocket

The original REST API documentation is available [here](https://wikiconnect.thefirstock.com/).

### Login
For the Login process we require to generate the appkey and vendor code by logging in with the firstock credentials in the give link [Key Generation](https://connect.thefirstock.com/login).

```python
from thefirstock import thefirstock

login = thefirstock.firstock_login(
    userId="{{userID}}",
    password="{{Password}}",
    TOTP="{{TOTP}}",
    vendorCode="{{vendorCode}}",
    apiKey="{{apiKey}}",
  )
```

### Place Order

```python
from thefirstock import thefirstock

placeOrder = thefirstock.firstock_placeOrder(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="ITC-EQ",
    quantity="1",
    price="300",
    product="I",
    transactionType="B",
    priceType="LMT",
    retention="DAY",
    triggerPrice="0",
    remarks="Python Package Order"
)
```

### Time Price Series

```python
from thefirstock import thefirstock

timePriceSeries = thefirstock.firstock_TimePriceSeries(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="Nifty 50",
    startTime="13/02/2023 09:45:45",
    endTime="13/12/2023 13:56:34",
    interval="30"
)
```

Refer to the Firstock Connect Documentation for the complete list of supported methods.

## WebSocket usage
In Version 4 there is a major feature where the websocket now can be run in background as a thread. 
In the below first example you can see the websocket without running in background. 

```python
from thefirstock import thefirstock


handler = thefirstock.WebSocketHandler("{userId}")
listOfTradingSymbol = ["Nifty Bank", "Nifty 50"]


def subscribe_feed_data(data):
    print(data)


# Modify the websocket_connection function to accept the handler as an argument
thread = thefirstock.websocket_connection(
    handler,
    listOfTradingSymbol,
    socket_connection=1,
    activate_sub_feed=True,
    callback_sub_feed=subscribe_feed_data
)
```

To subscribe and unsubscribe to symbols while the websocket is initiated
```python
from thefirstock import thefirstock


handler = thefirstock.WebSocketHandler("{userId}")
listOfTradingSymbol = ["Nifty Bank", "Nifty 50"]


def subscribe_feed_data(data):
    thefirstock.subscribe_symbol(handler, "ACC-EQ")
    thefirstock.unsubscribe_symbol(handler, "Nifty 50")
    print(data)


# Modify the websocket_connection function to accept the handler as an argument
thread = thefirstock.websocket_connection(
    handler,
    listOfTradingSymbol,
    socket_connection=1,
    activate_sub_feed=True,
    callback_sub_feed=subscribe_feed_data
)
```

To run websocket in background
```python
from thefirstock import thefirstock


handler = thefirstock.WebSocketHandler("PV0013")
listOfTradingSymbol = ["Nifty Bank", "Nifty 50"]


def subscribe_feed_data(data):
    print(data)


# Modify the websocket_connection function to accept the handler as an argument
thread = thefirstock.websocket_connection(
    handler,
    listOfTradingSymbol,
    socket_connection=1,
    activate_sub_feed=True,
    callback_sub_feed=subscribe_feed_data,
    run_in_background=True
)

if thread:
    thread.join()

```

Refer to the Firstock Connect Documentation for the complete list of supported methods.

## Changelog
* The Python package has been updated to automatically convert passwords into SHA256 hashes prior to submission to the login URL. 


* The package now includes a multi-login feature, enabling simultaneous login for multiple users, with each user's session being individually stored. 


* For all APIs, it is now required to pass the userId. The corresponding jKey session linked to the userId will be utilized for executing the API.


* The following methods have been updated to require trading symbols instead of tokens:
  * Get Multi Quotes LTP 
  * Get Multi Quotes 
  * Day Interval Time Price Series 
  * Time Price Series 
  * Security Info 
  * Get Quotes 


* The method for accessing the websocket has been entirely revamped. Detailed information will be available in an upcoming blog post. Additionally, sample code illustrating the new method can be found in the examples section.
