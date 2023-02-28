"""
The data source for all login/logout and user requests
"""
import copy
from ...utils.datasources import NorenRestDataSource
from . import endpoints
from hashlib import sha256

from .models import *

class UserDataSource(NorenRestDataSource):
  """
  The data source for all login/logout and user requests.
  """

  def login(self, model: LoginRequestModel) -> LoginResponseModel.update_forward_refs():
    """
    Login to the system using password or device pin.
      - If model contains the 'pwd' value login using normal login request.
      - If model contains the 'dpin' value login using device pin login request.

    Args:
      model (LoginRequestModel): The data to be send as LoginRequestModel.

    Returns:
      LoginResponseModel: The response from login request as LoginResponseModel.
    """
    request_model = copy.deepcopy(model)

    app_key = request_model.uid + "|" + request_model.appkey
    hash_fn = sha256()
    hash_fn.update(app_key.encode())
    request_model.appkey = hash_fn.hexdigest()

    # convert request model to json string
    request_json = request_model.json(exclude_unset=True)
    # get the endpint based on secret provided
    url = endpoints.LOGIN if request_model.pwd is not None else endpoints.LOGIN_WITH_DPIN
    # send the post request to get the json response
    response_json = self.post(url, f"jData={request_json}")
    print(type(response_json))
    # convert the request to response model
    return LoginResponseModel.parse_raw(response_json)

  def validate_hs_token(self, login_id: str, token: str) -> bool:
    """
    Check if the given HS token is valid or not

    Args:
      login_id (str): The sLoginId received from Initiator site,
      token (str): The HS token obtained

    Returns:
      bool: Whether the given token is valid or not
    """
    # send the post request to get the text response
    response = self.post(endpoints.VERIFY_HS_TOKEN, f"LoginId={login_id}&token={token}")
    # convert the response text to boolean
    return response.strip() == 'TRUE'


  def save_fcm_token(self, model: SaveFCMTokenRequestModel, key: str = None) -> SaveFCMTokenResponseModel:
    """
    Send request to save FCM token

    Args:
      model (SaveFCMTokenRequestModel): The data to be send as SaveFCMTokenRequestModel
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SaveFCMTokenResponseModel: The response as SaveFCMTokenResponseModel.
    """
    response_json = self._run_request(model, endpoints.SAVE_FCM_TOKEN, key)
    # convert the request to response model
    return SaveFCMTokenResponseModel.parse_raw(response_json)