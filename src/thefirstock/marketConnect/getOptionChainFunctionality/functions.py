from thefirstock.Variables.common_imports import *
from thefirstock.marketConnect.getOptionChainFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetOptionChain(self, tsym, exch, strprc, cnt, userId):
        """
        :return:
        """
        url = GETOPTIONCHAIN

        with open(CONFIG_PATH) as file:
            config_data = json.load(file)

        if userId in config_data:
            payload = {
                "userId": userId,
                "exchange": exch,
                "tradingSymbol": tsym,
                "strikePrice": strprc,
                "count": cnt,
                "jKey": config_data[userId]['jKey']
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        return not_logged_in_user()
