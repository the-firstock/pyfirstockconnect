from thefirstock.marketConnect.spanCalculatorFunctionality.execution import *


def firstock_SpanCalculator(dataList):
    try:
        spanCalculator = FirstockSpanCalculator(
            dataList=dataList,
        ).firstockSpanCalculator()

        return spanCalculator

    except Exception as e:
        print(e)
