from thefirstock.Variables.common_imports import *
from thefirstock.marketConnect.optionGreekFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockOptionGreek(self, expiryDate: str, strikePrice: str, spotPrice: str, initRate: str,
                            volatility: str, optionType: str, userId:str):
        try:
            """
            :return: The json response
            """
            url = OPTIONGREEK

            with open(CONFIG_PATH) as file:
                config_data = json.load(file)

            if userId in config_data:

                payload = {
                    "userId": userId,
                    "expiryDate": expiryDate,
                    "strikePrice": strikePrice,
                    "spotPrice": spotPrice,
                    "initRate": initRate,
                    "volatility": volatility,
                    "optionType": optionType,
                    "jKey": config_data[userId]['jKey']
                }

                result = requests.post(url, json=payload)
                jsonString = result.content.decode("utf-8")

                finalResult = ast.literal_eval(jsonString)

                return finalResult

            return not_logged_in_user()

        except Exception as e:
            print(e)
