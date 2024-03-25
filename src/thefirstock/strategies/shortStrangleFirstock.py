from thefirstock.strategies.shortStrangle import *


def firstock_ShortStrangle(symbol: str, callStrikePrice: str, putStrikePrice: str, expiry: str, product: str, quantity: str, remarks: str,
                           hedge: bool, hedgeValue: int, userId:str):
    try:
        SS = firstock_short_strangle(
            symbol=symbol,
            callStrikePrice=callStrikePrice,
            putStrikePrice=putStrikePrice,
            hedge=hedge,
            hedgeValue=hedgeValue,
            expiry=expiry,
            product=product,
            quantity=quantity,
            remarks=remarks,
            userId=userId
        )

        return SS

    except Exception as e:
        print(e)
