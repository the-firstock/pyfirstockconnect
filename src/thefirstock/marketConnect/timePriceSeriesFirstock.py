from thefirstock.marketConnect.timePriceSeriesFunctionality.execution import *


def firstock_TimePriceSeries(exchange, tradingSymbol, startTime, endTime, interval, userId):
    try:

        timePrice = FirstockTimePriceSeries(
            exch=exchange,
            token=tradingSymbol,
            st=startTime,
            et=endTime,
            intrv=interval,
            userId=userId
        ).firstockTimePriceSeries()

        return timePrice

    except Exception as e:
        print(e)
