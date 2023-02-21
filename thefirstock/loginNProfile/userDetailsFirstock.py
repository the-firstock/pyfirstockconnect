from thefirstock.loginNProfile.userDetailsFunctionality.execution import *


def firstock_userDetails():
    try:
        userDetails = FirstockUserDetails().firstockUserDetails()

        return userDetails

    except Exception as e:
        print(e)
