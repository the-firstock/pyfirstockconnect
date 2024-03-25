from thefirstock.marketConnect.searchScripsFunctionality.execution import *


def firstock_SearchScrips(stext, userId):
    try:

        searchScrips = FirstockSearchScrips(
            stext=stext,
            userId=userId
        ).firstockSearchScrips()

        return searchScrips

    except Exception as e:
        print(e)
