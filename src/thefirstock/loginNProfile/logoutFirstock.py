from thefirstock.loginNProfile.logoutFunctionality.execution import *


def firstock_logout(userId):
    try:
        logout = FirstockLogout(userId).firstockLogout()
        return logout

    except Exception as e:
        print(e)
