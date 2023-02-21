import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.marketConnect.getOptionChainFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetOptionChain(self, tsym, exch, strprc, cnt):
        """
        :return:
        """
        url = GETOPTIONCHAIN

        with open("config.json") as file:
            data = json.load(file)

        uid = data["uid"]
        jKey = data["jKey"]

        payload = {
            "userId": uid,
            "exchange": exch,
            "tradingSymbol": tsym,
            "strikePrice": strprc,
            "count": cnt,
            "jKey": jKey
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
