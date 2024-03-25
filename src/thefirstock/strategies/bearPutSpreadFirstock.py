from thefirstock.strategies.bearPutSpread import *


def firstock_BearPutSpread(symbol: str, putBuyStrikePrice: str, putSellStrikePrice: str, expiry: str,
                           product: str, quantity: str, remarks: str, userId:str):
    try:
        BPS = firstock_bear_put_spread(
            symbol=symbol,
            putBuyStrikePrice=putBuyStrikePrice,
            putSellStrikePrice=putSellStrikePrice,
            expiry=expiry,
            product=product,
            quantity=quantity,
            remarks=remarks,
            userId=userId
        )

        return BPS

    except Exception as e:
        print(e)
