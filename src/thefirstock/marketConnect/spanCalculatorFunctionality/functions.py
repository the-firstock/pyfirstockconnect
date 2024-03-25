from thefirstock.Variables.common_imports import *
from thefirstock.marketConnect.spanCalculatorFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockSpanCalculator(self, dataList, userId):
        """
        :return:
        """
        url = SPANCALCULATOR

        with open(CONFIG_PATH) as file:
            config_data = json.load(file)

        if userId in config_data:

            payload = {
                "userId": userId,
                "jKey": config_data[userId]['jKey'],
                "data": dataList
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult

        return not_logged_in_user()
