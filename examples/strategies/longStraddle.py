from thefirstock import thefirstock

LS = thefirstock.firstock_LongStraddle(
    symbol="NIFTY",
    strikePrice="18000",
    expiry="23FEB23",
    product="C",
    quantity="10",
    remarks="Hello"
)

print(LS)
