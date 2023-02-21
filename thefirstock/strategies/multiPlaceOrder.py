import ast
import json
import requests

from thefirstock.Variables.enums import *


def firstock_multi_placeOrder(dataList: list):

    url = MULTIPLACEORDER

    with open("config.json") as file:
        data = json.load(file)

    uid = data["uid"]
    jKey = data["jKey"]

    payload = {
        "data": dataList,
        "jKey": jKey,
        "userId": uid
    }

    result = requests.post(url, json=payload)
    jsonString = result.content.decode("utf-8")

    finalResult = ast.literal_eval(jsonString)

    return finalResult
