import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.ordersNReport.orderMarginFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetOrderMargin(self, exch, tsym, qty, prc, prd, trantype, prctyp):
        """
        :return:
        """
        try:
            url = ORDERMARGIN

            with open("config.json") as file:
                data = json.load(file)

            uid = data["uid"]
            jKey = data["jKey"]

            payload = {
                "userId": uid,
                "actid": uid,
                "exchange": exch,
                "tradingSymbol": tsym,
                "quantity": qty,
                "price": prc,
                "product": prd,
                "transactionType": trantype,
                "priceType": prctyp,
                "jKey": jKey
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
