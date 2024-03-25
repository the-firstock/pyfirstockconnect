from thefirstock.Variables.common_imports import *
from thefirstock.loginNProfile.userDetailsFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockUserDetails(self, uid):
        """
        :return: The json response
        """
        url = USERDETAILS

        with open(CONFIG_PATH) as file:
            config_data = json.load(file)

        if uid in config_data:
            payload = {
                "userId": uid,
                "jKey": config_data[uid]['jKey']
            }

            result = requests.post(url, json=payload)
            jsonString = result.content.decode("utf-8")

            finalResult = ast.literal_eval(jsonString)

            return finalResult
        return not_logged_in_user()
