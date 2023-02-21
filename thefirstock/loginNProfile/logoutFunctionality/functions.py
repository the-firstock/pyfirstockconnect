import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.loginNProfile.logoutFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockLogout(self):
        """
        :return:
        """
        url = LOGOUT

        with open("config.json") as file:
            data = json.load(file)

        uid = data["uid"]
        jKey = data["jKey"]

        payload = {
            "userId": uid,
            "jKey": jKey
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
