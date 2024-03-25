from thefirstock.marketConnect.optionGreekFunctionality.execution import *


def firstock_OptionGreek(expiryDate, strikePrice, spotPrice, initRate, volatility, optionType, userId):
    try:
        optionGreek = FirstockOptionGreek(
            expiryDate=expiryDate,
            strikePrice=strikePrice,
            spotPrice=spotPrice,
            initRate=initRate,
            volatility=volatility,
            optionType=optionType,
            userId=userId
        )

        result = optionGreek.firstockOptionGreek()
        return result

    except Exception as e:
        print(e)
