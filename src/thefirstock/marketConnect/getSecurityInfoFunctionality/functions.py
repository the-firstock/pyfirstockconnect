from thefirstock.Variables.common_imports import *
from thefirstock.marketConnect.getSecurityInfoFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetSecurityInfo(self, exch, token, userId):
        """
        :return:
        """
        try:
            url = GETSECURITYINFO

            with open(CONFIG_PATH) as file:
                config_data = json.load(file)

            if userId in config_data:
                payload = {
                    "userId": userId,
                    "exchange": exch,
                    "tradingSymbol": token,
                    "jKey": config_data[userId]['jKey']
                }

                result = requests.post(url, json=payload)
                jsonString = result.content.decode("utf-8")

                finalResult = ast.literal_eval(jsonString)

                return finalResult
            return not_logged_in_user()
        except Exception as e:
            print(e)
