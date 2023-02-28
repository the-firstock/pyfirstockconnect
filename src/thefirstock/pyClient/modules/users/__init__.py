"""
User Module
===========

This module contains the `datasource` and `models` required for user module.
This datasource is initialized inside the `client` and can be accessed by `client.users` property.

Usage
-----
```py
from pyClient.modules.users import UserDataSource, LoginRequestModel

appstate = {}

users = new UserDataSource(base_url='https://yourapi.url/namespace/', state=appstate)

model = LoginRequestModel(...)
users.login(model)
```
"""

from .datasource import *
from .models import *