import ast
import json
import requests

from thefirstock.Variables.enums import *


def firstock_long_strangle(symbol: str, callStrikePrice: str, putStrikePrice: str, expiry: str, product: str, quantity: str, remarks: str):

    url = LONGSTRANGLE

    with open("config.json") as file:
        data = json.load(file)

    uid = data["uid"]
    jKey = data["jKey"]

    payload = {
        "symbol": symbol,
        "callStrikePrice": callStrikePrice,
        "putStrikePrice": putStrikePrice,
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
