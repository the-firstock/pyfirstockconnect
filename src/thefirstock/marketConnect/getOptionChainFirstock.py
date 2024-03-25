from thefirstock.marketConnect.getOptionChainFunctionality.execution import *


def firstock_OptionChain(tradingSymbol, exchange, strikePrice, count, userId):
    try:

        optionChain = FirstockGetOptionChain(
            tsym=tradingSymbol,
            exch=exchange,
            strprc=strikePrice,
            cnt=count,
            userId=userId
        ).firstockGetOptionChain()

        return optionChain

    except Exception as e:
        print(e)
