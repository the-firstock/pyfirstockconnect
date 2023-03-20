import ast
import json
import requests

from thefirstock.Variables.enums import *
from thefirstock.marketConnect.getMultiQuoteLTPFuntionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetMultiQuoteLTP(self, dataToken):
        """
        :return:
        """
        try:
            url = GETMULTIQUOTESLTP

            with open("config.json") as file:
                data = json.load(file)

            uid = data["uid"]
            jKey = data["jKey"]

            payload = {
                "userId": uid,
                "data": dataToken,
                "jKey": jKey
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
