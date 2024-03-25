from thefirstock.Variables.common_imports import *
from thefirstock.ordersNReport.orderMarginFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockGetOrderMargin(self, exch, tsym, qty, prc, prd, trantype, prctyp, userId):
        """
        :return:
        """
        try:
            url = ORDERMARGIN

            with open(CONFIG_PATH) as file:
                config_data = json.load(file)

            if userId in config_data:
                payload = {
                    "userId": userId,
                    "actid": userId,
                    "exchange": exch,
                    "tradingSymbol": tsym,
                    "quantity": qty,
                    "price": prc,
                    "product": prd,
                    "transactionType": trantype,
                    "priceType": prctyp,
                    "jKey": config_data[userId]['jKey']
                }

                result = requests.post(url, json=payload)
                jsonString = result.content.decode("utf-8")

                finalResult = ast.literal_eval(jsonString)

                return finalResult
            return not_logged_in_user()
        except Exception as e:
            print(e)
