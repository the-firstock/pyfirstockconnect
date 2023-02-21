from thefirstock.loginNProfile.userDetailsFunctionality.functions import *


class FirstockUserDetails:
    def __init__(self):
        self.userDetails = ApiRequests()

    def firstockUserDetails(self):
        result = self.userDetails.firstockUserDetails()
        return result
