from thefirstock.loginNProfile.userDetailsFunctionality.execution import *


def firstock_userDetails(userId):
    try:
        userDetails = FirstockUserDetails(userId).firstockUserDetails()

        return userDetails

    except Exception as e:
        print(e)
