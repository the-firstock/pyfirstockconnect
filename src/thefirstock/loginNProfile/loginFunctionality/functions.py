import hashlib

from thefirstock.Variables.common_imports import *
from thefirstock.loginNProfile.loginFunctionality.base import *


def encodePwd(pwd):
    """
    :param pwd:
    :return:
    """
    return hashlib.sha256((pwd.encode()))


class ApiRequests(FirstockAPI):
    def firstockLogin(self, uid: str, pwd: str, factor2: str, vc: str, appkey: str):
        """
        :return: The json response
        """
        url = LOGIN
        encryptedPassword = encodePwd(pwd)

        payload = {
            "userId": uid,
            "password": encryptedPassword.hexdigest(),
            "TOTP": factor2,
            "vendorCode": vc,
            "apiKey": appkey
        }

        result = requests.post(url, json=payload)
        jsonString = result.content.decode("utf-8")

        finalResult = ast.literal_eval(jsonString)

        if "status" in finalResult:
            if finalResult["status"] == "success":
                if not os.path.exists(CONFIG_PATH):
                    with open(CONFIG_PATH, "w") as config_file:
                        # You can write initial content to the file if needed
                        config_file.write("{}")

                with open(CONFIG_PATH, "r") as infile:
                    try:
                        in_json = json.load(infile)
                    except Exception:
                        in_json = {}

                    in_json[f"{uid}"] = {"jKey": finalResult["data"]["susertoken"]}

                jsonObject = json.dumps(in_json, indent=4)

                with open(CONFIG_PATH, "w") as outfile:
                    outfile.write(jsonObject)
                return finalResult

            elif finalResult["status"] == "failed":
                return finalResult
