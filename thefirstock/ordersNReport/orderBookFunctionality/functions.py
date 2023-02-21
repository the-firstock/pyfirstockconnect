import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.ordersNReport.orderBookFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockOrderBook(self):
        """
        :return:
        """
        try:
            url = ORDERBOOK

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

        except Exception as e:
            print(e)
