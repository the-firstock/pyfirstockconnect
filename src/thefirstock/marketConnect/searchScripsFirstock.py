from thefirstock.marketConnect.searchScripsFunctionality.execution import *


def firstock_SearchScrips(stext):
    try:

        searchScrips = FirstockSearchScrips(
            stext=stext
        ).firstockSearchScrips()

        return searchScrips

    except Exception as e:
        print(e)
