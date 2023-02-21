"""
The REST data source which fetch data from rest api endpoints.
"""
import requests
from typing import Any, Dict, List
from urllib.parse import urlparse, urljoin
from functools import reduce

from .context import RestContext
from ....common.enums import RestMethod
from ...interceptors import Interceptor
from ...stateful import Stateful

__all__ = [
    'RestDataSource'
]


class RestDataSource(Stateful):
    """
  The REST data source which fetch data from rest api endpoints.
  """

    def __init__(
            self,
            base_url: str = None,
            interceptors: List[Interceptor] = [],
            state: Dict[str, Any] = {},
            headers: dict = {}) -> None:
        """
    Initialize the RestDataSource

    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.
    """
        super().__init__(state)
        self._base_url = base_url if base_url.endswith('/') else base_url + '/'
        self._headers = {
            'Content-Type': 'text/plain',
            **headers
        }
        self._interceptors = interceptors

    def post(self, url: str, data: str, params: Dict[str, str] = {}, headers: Dict[str, str] = {}, **kwargs):
        """
    Send a post request a url and return a json response

    Args:
        url (str): The endpoint url
        json (str): The json payload
        params (Dict[str, str]): The query parameters
        headers (Dict[str, str]): The extra headers to pass to the request
    """
        headers = {**self._headers, **headers}
        url = self._expand_url(url)
        # create context
        context = RestContext(
            url=url,
            data=data,
            params=params,
            headers=headers,
            method=RestMethod.POST
        )
        # run interceptor's before hook
        context = self._intercept_before(context)
        # send post request
        response = requests.post(
            context.url, context.data, params=context.params, headers=context.headers, **kwargs)
        # add response and result to context
        context.response = response
        context.result = response.text
        # run interceptor's after hook
        context = self._intercept_after(context)
        return context.result

    def _intercept_before(self, context: RestContext):
        """
        Run the interceptor's before hook on the context

        Args:
          context (RestContext): The request context
        """

        def reducer(ctx: RestContext, interceptor: Interceptor[RestContext]):
            """
            The reducer for running interceptor before hook
            """
            return interceptor.before(ctx)

        # Run reducer over all the available interceptors
        return reduce(reducer, self._interceptors, context)

    def _intercept_after(self, context: RestContext):
        """
        Run the interceptor's after hook on the context

        Args:
          context (RestContext): The request context
        """

        def reducer(ctx: RestContext, interceptor: Interceptor[RestContext]):
            """
            The reducer for running interceptor after hook
            """
            return interceptor.after(ctx)

        # Run reducer over all the available interceptors
        return reduce(reducer, self._interceptors, context)

    def _expand_url(self, url: str):
        """
    Expand a given relative url if a base url exists
    """
        if self._base_url is not None:
            # check if the given url is relative or not
            if not bool(urlparse(url).netloc):
                url = urljoin(self._base_url, url)
        return url
