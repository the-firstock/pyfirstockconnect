from thefirstock import thefirstock

orderMargin = thefirstock.firstock_orderMargin(
    exchange="NSE",
    tradingSymbol="ITC-EQ",
    quantity="1",
    priceType="LMT",
    product="C",
    price="350",
    transactionType="B"
)
print(orderMargin)
