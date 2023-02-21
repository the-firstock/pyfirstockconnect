import ast
import json
import requests

from thefirstock.Variables.enums import *
from thefirstock.marketConnect.optionGreekFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockOptionGreek(self, expiryDate: str, strikePrice: str, spotPrice: str, initRate: str,
                            volatility: str, optionType: str):
        try:
            """
            :return: The json response
            """
            url = OPTIONGREEK

            with open("config.json") as file:
                data = json.load(file)

            jKey = data["jKey"]
            userId = data["uid"]

            payload = {
                "userId": userId,
                "expiryDate": expiryDate,
                "strikePrice": strikePrice,
                "spotPrice": spotPrice,
                "initRate": initRate,
                "volatility": volatility,
                "optionType": optionType,
                "jKey": jKey
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        except Exception as e:
            print(e)
