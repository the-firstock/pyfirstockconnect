import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.ordersNReport.modifyOrderFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockModifyOrder(self, qty, orderNumber, trgprc, prc, exchange, tradingSymbol, priceType):
        """
        :return:
        """
        try:
            url = MODIFYORDER

            with open("config.json") as file:
                data = json.load(file)

            uid = data["uid"]
            jKey = data["jKey"]

            payload = {
                "userId": uid,
                "orderNumber": orderNumber,
                "quantity": qty,
                "price": prc,
                "triggerPrice": trgprc,
                "exchange": exchange,
                "tradingSymbol": tradingSymbol,
                "priceType": priceType,
                "jKey": jKey
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
