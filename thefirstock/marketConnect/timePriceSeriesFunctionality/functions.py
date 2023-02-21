import ast
import json
import requests

from thefirstock.Variables.enums import *
from thefirstock.marketConnect.timePriceSeriesFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockTimePriceSeries(self, exch, token, st, et, intrv):
        """
        :return:
        """
        url = TIMEPRICESERIES

        with open("config.json") as file:
            data = json.load(file)

        uid = data["uid"]
        jKey = data["jKey"]

        payload = {
            "userId": uid,
            "exchange": exch,
            "token": token,
            "endTime": et,
            "startTime": st,
            "jKey": jKey,
            "interval": intrv
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
