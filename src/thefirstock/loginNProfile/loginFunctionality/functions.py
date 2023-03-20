import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.loginNProfile.loginFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockLogin(self, uid: str, pwd: str, factor2: str, vc: str, appkey: str):
        """
        :return: The json response
        """
        url = LOGIN

        payload = {
            "userId": uid,
            "password": pwd,
            "TOTP": factor2,
            "vendorCode": vc,
            "apiKey": appkey
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        if "status" in finalResult:
            if finalResult["status"] == "Success":
                dictionary = {
                    "uid": uid,
                    "jKey": finalResult["data"]["susertoken"]
                }

                jsonObject = json.dumps(dictionary, indent=4)

                with open("config.json", "w") as outfile:
                    outfile.write(jsonObject)
                return finalResult

            elif finalResult["status"] == "Failed":
                return finalResult
