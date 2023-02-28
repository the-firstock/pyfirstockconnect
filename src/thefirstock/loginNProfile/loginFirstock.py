from thefirstock.loginNProfile.loginFunctionality.execution import *


def firstock_login(userId, password, TOTP, vendorCode, apiKey):
    try:
        login = FirstockLogin(
            uid=userId,
            pwd=password,
            factor2=TOTP,
            vc=vendorCode,
            appkey=apiKey,
        )

        result = login.firstockLogin()

        return result

    except Exception as e:
        print(e)
