from thefirstock.marketConnect.optionGreekFunctionality.functions import *


class FirstockOptionGreek:
    def __init__(self, expiryDate, strikePrice, spotPrice, initRate, volatility, optionType):
        self.optionGreek = ApiRequests()

        self.expiryDate = expiryDate
        self.strikePrice = strikePrice
        self.spotPrice = spotPrice
        self.initRate = initRate
        self.volatility = volatility
        self.optionType = optionType

    def firstockOptionGreek(self):
        result = self.optionGreek.firstockOptionGreek(self.expiryDate, self.strikePrice,
                                                      self.spotPrice, self.initRate, self.volatility,
                                                      self.optionType)
        return result
