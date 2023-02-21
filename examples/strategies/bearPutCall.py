from thefirstock import thefirstock

BPS = thefirstock.firstock_BearPutSpread(
    symbol="NIFTY",
    putBuyStrikePrice="18000",
    putSellStrikePrice="17800",
    expiry="23FEB23",
    product="C",
    quantity="10",
    remarks="Hello"
)

print(BPS)
