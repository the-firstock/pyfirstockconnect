from thefirstock.Variables.common_imports import *
from thefirstock.marketConnect.getMultiQuoteFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetMultiQuote(self, dataToken, userId):
        """
        :return:
        """
        try:
            url = GETMULTIQUOTES

            with open(CONFIG_PATH) as file:
                config_data = json.load(file)

            if userId in config_data:
                payload = {
                    "userId": userId,
                    "data": dataToken,
                    "jKey": config_data[userId]['jKey']
                }

                result = requests.post(url, json=payload)
                jsonString = result.content.decode("utf-8")

                finalResult = ast.literal_eval(jsonString)

                return finalResult
            return not_logged_in_user()
        except Exception as e:
            print(e)
