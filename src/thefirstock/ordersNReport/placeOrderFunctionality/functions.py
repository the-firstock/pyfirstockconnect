import ast
import json
import requests

from thefirstock.Variables.enums import *

from thefirstock.ordersNReport.placeOrderFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockPlaceOrder(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks):
        """
        :return:
        """
        url = PLACEORDER

        with open("config.json") as file:
            data = json.load(file)

        uid = data["uid"]
        jKey = data["jKey"]

        payload = {
            "userId": uid,
            "exchange": exch,
            "tradingSymbol": tsym,
            "quantity": qty,
            "price": prc,
            "product": prd,
            "transactionType": trantype,
            "priceType": prctyp,
            "retention": ret,
            "triggerPrice": trgprc,
            "remarks": remarks,
            "jKey": jKey
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
