import ast
import json
import requests

from thefirstock.marketConnect.getIndexListFunctionality.base import *

from thefirstock.Variables.enums import *


class ApiRequests(FirstockAPI):
    def firstockGetIndexList(self, exch):
        """
                :return:
                """
        try:
            url = GETINDEXLIST

            with open("config.json") as file:
                data = json.load(file)

            uid = data["uid"]
            jKey = data["jKey"]

            payload = {
                "userId": uid,
                "exchange": exch,
                "jKey": jKey
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
