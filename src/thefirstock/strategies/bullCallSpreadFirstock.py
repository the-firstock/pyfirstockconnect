from thefirstock.strategies.bullCallSpread import *


def firstock_BullCallSpread(symbol: str, callBuyStrikePrice: str, callSellStrikePrice: str, expiry: str,
                            product: str, quantity: str, remarks: str):
    try:
        BCS = firstock_bull_call_spread(
            symbol=symbol,
            callBuyStrikePrice=callBuyStrikePrice,
            callSellStrikePrice=callSellStrikePrice,
            expiry=expiry,
            product=product,
            quantity=quantity,
            remarks=remarks
        )

        return BCS

    except Exception as e:
        print(e)
