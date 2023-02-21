from thefirstock.strategies.longStrangle import *


def firstock_LongStrangle(symbol: str, callStrikePrice: str, putStrikePrice: str, expiry: str,
                            product: str, quantity: str, remarks: str):
    try:
        LS = firstock_long_strangle(
            symbol=symbol,
            callStrikePrice=callStrikePrice,
            putStrikePrice=putStrikePrice,
            expiry=expiry,
            product=product,
            quantity=quantity,
            remarks=remarks
        )

        return LS

    except Exception as e:
        print(e)
