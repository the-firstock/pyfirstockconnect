from thefirstock.marketConnect.spanCalculatorFunctionality.functions import *


class FirstockSpanCalculator:
    def __init__(self, dataList):
        self.spanCalculator = ApiRequests()

        self.dataList = dataList

    def firstockSpanCalculator(self):
        result = self.spanCalculator.firstockSpanCalculator(self.dataList)

        return result
