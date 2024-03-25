from thefirstock.marketConnect.spanCalculatorFunctionality.functions import *


class FirstockSpanCalculator:
    def __init__(self, dataList, userId):
        self.spanCalculator = ApiRequests()
        self.userId = userId
        self.dataList = dataList

    def firstockSpanCalculator(self):
        result = self.spanCalculator.firstockSpanCalculator(self.dataList, self.userId)

        return result
