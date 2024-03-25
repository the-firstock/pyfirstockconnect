from thefirstock.loginNProfile.logoutFunctionality.functions import *


class FirstockLogout:
    def __init__(self, uid):
        self.logoutDetails = ApiRequests()
        self.uid = uid

    def firstockLogout(self):
        result = self.logoutDetails.firstockLogout(self.uid)
        return result
