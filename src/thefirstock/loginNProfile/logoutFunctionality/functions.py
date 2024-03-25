from thefirstock.Variables.common_imports import *
from thefirstock.loginNProfile.logoutFunctionality.base import *


class ApiRequests(FirstockAPI):
    def firstockLogout(self, uid):
        """
        :return:
        """
        url = LOGOUT

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
            if finalResult['status'] == 'Success':
                del config_data[uid]
                with open(CONFIG_PATH, "w") as outfile:
                    outfile.write(json.dumps(config_data, indent=4))
            return finalResult

        return not_logged_in_user()
