import ast
import json
import requests

from thefirstock.loginNProfile.userDetailsFunctionality.base import *

from thefirstock.Variables.enums import *


class ApiRequests(FirstockAPI):
    def firstockUserDetails(self):
        """
        :return: The json response
        """
        url = USERDETAILS

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
