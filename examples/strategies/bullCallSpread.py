from thefirstock import thefirstock

BCS = thefirstock.firstock_BullCallSpread(
    symbol="NIFTY",
    callBuyStrikePrice="18000",
    callSellStrikePrice="17800",
    expiry="23FEB23",
    product="C",
    quantity="15",
    remarks="Hello"
)

print(BCS)
