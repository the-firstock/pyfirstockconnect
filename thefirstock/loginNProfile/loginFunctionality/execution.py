from thefirstock.loginNProfile.loginFunctionality.functions import *


class FirstockLogin:
    def __init__(self, uid, pwd, factor2, vc, appkey):
        self.loginDetails = ApiRequests()
        self.uid = uid
        self.pwd = pwd
        self.factor2 = factor2
        self.vc = vc
        self.appkey = appkey

    def firstockLogin(self):
        result = self.loginDetails.firstockLogin(self.uid, self.pwd, self.factor2, self.vc, self.appkey)
        return result
