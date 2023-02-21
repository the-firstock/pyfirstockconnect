from thefirstock import thefirstock

LS = thefirstock.firstock_LongStrangle(
    symbol="NIFTY",
    callStrikePrice="18000",
    putStrikePrice="17800",
    expiry="23FEB23",
    product="C",
    quantity="10",
    remarks="Hello"
)

print(LS)
