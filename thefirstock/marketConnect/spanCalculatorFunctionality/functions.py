import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.marketConnect.spanCalculatorFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockSpanCalculator(self, dataList):
        """
        :return:
        """
        url = SPANCALCULATOR

        with open("config.json") as file:
            data = json.load(file)

        uid = data["uid"]
        jKey = data["jKey"]

        payload = {
            "userId": uid,
            "jKey": jKey,
            "data": dataList
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
