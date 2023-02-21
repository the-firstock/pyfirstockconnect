"""
Data sources for noren requests
"""
from pydantic import BaseModel
from ..rest import RestDataSource


class NorenRestDataSource(RestDataSource):
    """
  The rest datasource for noren apis
  """

    def _run_request(self, model: BaseModel, endpoint: str, key: str = None):
        """
    Private function to run a post request with key
    """
        # get key from saved state if not passed explicitly
        key = self.get_state('token', key)
        # convert request model to json string
        request_json = model.json(exclude_unset=True)
        # send the post request to get the json response
        return self.post(endpoint, f"jData={request_json}&jKey={key}")
