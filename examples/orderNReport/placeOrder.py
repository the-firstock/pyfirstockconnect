from thefirstock import thefirstock

placeOrder = thefirstock.firstock_placeOrder(
    exchange="NSE",
    tradingSymbol="ITC-EQ",
    quantity="1",
    price="300",
    product="I",
    transactionType="B",
    priceType="LMT",
    retention="DAY",
    triggerPrice="",
    remarks="Python Package Order"
)
print(placeOrder)
