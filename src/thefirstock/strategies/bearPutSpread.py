import ast
import json
import requests

from thefirstock.Variables.enums import *


def firstock_bear_put_spread(symbol: str, putBuyStrikePrice: str, putSellStrikePrice: str, expiry: str,
                             product: str, quantity: str, remarks: str):
    """
    :param symbol:
    :param putBuyStrikePrice:
    :param putSellStrikePrice:
    :param expiry:
    :param product:
    :param quantity:
    :param remarks:
    :return:
    """

    url = BEARPUTSPREAD

    with open("config.json") as file:
        data = json.load(file)

    uid = data["uid"]
    jKey = data["jKey"]

    payload = {
        "symbol": symbol,
        "putBuyStrikePrice": putBuyStrikePrice,
        "putSellStrikePrice": putSellStrikePrice,
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
