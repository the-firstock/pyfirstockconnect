from thefirstock.marketConnect.getOptionChainFunctionality.execution import *


def firstock_OptionChain(tradingSymbol, exchange, strikePrice, count):
    try:

        optionChain = FirstockGetOptionChain(
            tsym=tradingSymbol,
            exch=exchange,
            strprc=strikePrice,
            cnt=count
        ).firstockGetOptionChain()

        return optionChain

    except Exception as e:
        print(e)