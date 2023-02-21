from thefirstock import thefirstock

SS = thefirstock.firstock_ShortStrangle(
    symbol="NIFTY",
    callStrikePrice="18000",
    putStrikePrice="17800",
    expiry="23FEB23",
    product="C",
    quantity="10",
    remarks="Hello",
    hedgeValue=300,
    hedge=True
)

print(SS)
