"""
The client combines all the modules and abstracts the inner logic
"""

from thefirstock.pyClient.websocket.client import WsClient
from .modules.users import LoginRequestModel
from .modules.users import UserDataSource
from .utils.stateful import Stateful

__all__ = ['Client']


class Client(Stateful):
    """
  The python client for communicating with external api
  """

    def __init__(self, socket_url: str) -> None:
        """
    Initialize the client

    Args:
      base_url (str, optional): The base url for the rest api endpoint. Defaults to None.
    """
        super().__init__({
            "token": None
        })
        self.__setup__()
        self.__ws = WsClient(socket_url, state=self.state)

    def __setup__(self) -> None:
        """
    Initial setup for the client
    """
        self._interceptors = []

    @property
    def ws(self) -> WsClient:
        """
    The websocket client
    """
        return self.__ws

    @property
    def state(self):
        """The current client state"""
        return self.__state__

    def login(self, response):
        """
    Login user. Alias for ```client.users.login```

    Args:
      model (LoginRequestModel): The data to be send as LoginRequestModel instance.

    Returns:
      LoginResponseModel: The response from login request as LoginResponseModel instance.
    """
        if response["jKey"] is not None:
            self.set_state('token', response["jKey"])
        return response
