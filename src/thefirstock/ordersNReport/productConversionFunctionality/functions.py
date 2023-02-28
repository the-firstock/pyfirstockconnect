import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.ordersNReport.productConversionFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockConvertProduct(self, exch, tsym, qty, prd, prevprd, trantype, postype):
        """
        :return:
        """
        try:
            url = PRODUCTCONVERSION

            with open("config.json") as file:
                data = json.load(file)

            uid = data["uid"]
            jKey = data["jKey"]

            payload = {
                "userId": uid,
                "exchange": exch,
                "tradingSymbol": tsym,
                "quantity": qty,
                "actid": uid,
                "product": prd,
                "previousProduct": prevprd,
                "transactionType": trantype,
                "positionType": postype,
                "jKey": jKey
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
