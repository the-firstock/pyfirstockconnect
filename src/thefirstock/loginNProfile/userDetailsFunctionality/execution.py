from thefirstock.loginNProfile.userDetailsFunctionality.functions import *


class FirstockUserDetails:
    def __init__(self, uid):
        self.userDetails = ApiRequests()
        self.uid = uid

    def firstockUserDetails(self):
        result = self.userDetails.firstockUserDetails(self.uid)
        return result
