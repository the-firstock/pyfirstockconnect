from thefirstock.strategies.shortStraddle import *


def firstock_ShortStraddle(symbol: str, strikePrice: str, expiry: str, product: str, quantity: str, remarks: str,
                           hedge: bool, hedgeValue: int):
    try:
        SS = firstock_short_straddle(
            symbol=symbol,
            strikePrice=strikePrice,
            hedge=hedge,
            hedgeValue=hedgeValue,
            expiry=expiry,
            product=product,
            quantity=quantity,
            remarks=remarks
        )

        return SS

    except Exception as e:
        print(e)
