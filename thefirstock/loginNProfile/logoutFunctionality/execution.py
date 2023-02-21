from thefirstock.loginNProfile.logoutFunctionality.functions import *


class FirstockLogout:
    def __init__(self):
        self.logoutDetails = ApiRequests()

    def firstockLogout(self):
        result = self.logoutDetails.firstockLogout()
        return result
