import ast
import json
import requests

from thefirstock.Variables.enums import *


def firstock_bull_call_spread(symbol: str, callBuyStrikePrice: str, callSellStrikePrice: str, expiry: str,
                             product: str, quantity: str, remarks: str):

    url = BULLCALLSPREAD

    with open("config.json") as file:
        data = json.load(file)

    uid = data["uid"]
    jKey = data["jKey"]

    payload = {
        "symbol": symbol,
        "callBuyStrikePrice": callBuyStrikePrice,
        "callSellStrikePrice": callSellStrikePrice,
        "expiry": expiry,
        "product": product,
        "quantity": quantity,
        "remarks": remarks,
        "jKey": jKey,
        "userId": uid
    }

    result = requests.post(url, json=payload)
    jsonString = result.content.decode("utf-8")

    finalResult = ast.literal_eval(jsonString)

    return finalResult
