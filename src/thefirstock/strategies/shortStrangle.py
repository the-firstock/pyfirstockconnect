from thefirstock.Variables.common_imports import *


def firstock_short_strangle(symbol: str, callStrikePrice: str, putStrikePrice: str, expiry: str, product: str,
                            quantity: str, remarks: str,
                            hedge: bool, hedgeValue: int, userId: str):
    url = SHORTSTRANGLE

    with open(CONFIG_PATH) as file:
        config_data = json.load(file)

    if userId in config_data:
        payload = {
            "symbol": symbol,
            "callStrikePrice": callStrikePrice,
            "putStrikePrice": putStrikePrice,
            "expiry": expiry,
            "product": product,
            "quantity": quantity,
            "remarks": remarks,
            "jKey": config_data[userId]['jKey'],
            "userId": userId,
            "hedge": hedge,
            "hedgeValue": hedgeValue,
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
    return not_logged_in_user()
