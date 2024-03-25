from thefirstock.marketConnect.spanCalculatorFunctionality.execution import *


def firstock_SpanCalculator(dataList, userId):
    try:
        spanCalculator = FirstockSpanCalculator(
            dataList=dataList,
            userId=userId
        ).firstockSpanCalculator()

        return spanCalculator

    except Exception as e:
        print(e)
