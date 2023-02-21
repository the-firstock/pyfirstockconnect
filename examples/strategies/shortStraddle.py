from thefirstock import thefirstock

SS = thefirstock.firstock_ShortStraddle(
    symbol="NIFTY",
    strikePrice="18000",
    expiry="23FEB23",
    product="C",
    quantity="10",
    remarks="Hello",
    hedgeValue=300,
    hedge=False
)

print(SS)
