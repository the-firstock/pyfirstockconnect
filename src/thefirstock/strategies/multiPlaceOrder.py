from thefirstock.Variables.common_imports import *


def firstock_multi_placeOrder(dataList: list, userId:str):

    url = MULTIPLACEORDER

    with open(CONFIG_PATH) as file:
        config_data = json.load(file)

    if userId in config_data:

        payload = {
            "data": dataList,
            "jKey": config_data[userId]['jKey'],
            "userId": userId
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        return finalResult
    return not_logged_in_user()