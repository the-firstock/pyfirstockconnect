from thefirstock.marketConnect.searchScripsFunctionality.functions import *


class FirstockSearchScrips:
    def __init__(self, stext):
        self.searchScrips = ApiRequests()
        self.stext = stext

    def firstockSearchScrips(self):
        result = self.searchScrips.firstockSearchScrips(self.stext)
        return result
