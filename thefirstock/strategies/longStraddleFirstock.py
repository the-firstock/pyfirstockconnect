from thefirstock.strategies.longStraddle import *


def firstock_LongStraddle(symbol: str, strikePrice: str, expiry: str,
                            product: str, quantity: str, remarks: str):
    try:
        LS = firstock_long_straddle(
            symbol=symbol,
            strikePrice=strikePrice,
            expiry=expiry,
            product=product,
            quantity=quantity,
            remarks=remarks
        )

        return LS

    except Exception as e:
        print(e)
