from thefirstock.Variables.common_imports import *
from thefirstock.ordersNReport.productConversionFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockConvertProduct(self, exch, tsym, qty, prd, prevprd, trantype, postype, userId):
        """
        :return:
        """
        try:
            url = PRODUCTCONVERSION

            with open(CONFIG_PATH) as file:
                config_data = json.load(file)

            if userId in config_data:
                payload = {
                    "userId": userId,
                    "exchange": exch,
                    "tradingSymbol": tsym,
                    "quantity": qty,
                    "actid": userId,
                    "product": prd,
                    "previousProduct": prevprd,
                    "transactionType": trantype,
                    "positionType": postype,
                    "jKey": config_data[userId]['jKey']
                }

                result = requests.post(url, json=payload)
                jsonString = result.content.decode("utf-8")

                finalResult = ast.literal_eval(jsonString)

                return finalResult
            return not_logged_in_user()

        except Exception as e:
            print(e)
