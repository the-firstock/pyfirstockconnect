from thefirstock.marketConnect.searchScripsFunctionality.functions import *


class FirstockSearchScrips:
    def __init__(self, stext, userId):
        self.searchScrips = ApiRequests()
        self.stext = stext
        self.userId = userId

    def firstockSearchScrips(self):
        result = self.searchScrips.firstockSearchScrips(self.stext, self.userId)
        return result
