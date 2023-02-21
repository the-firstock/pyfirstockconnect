from thefirstock import thefirstock

convertProduct = thefirstock.firstock_ConvertProduct(
    transactionType="B",
    tradingSymbol="ITC-EQ",
    quantity="1",
    product="C",
    previousProduct="I",
    positionType="DAY",
    exchange="NSE"
)
print(convertProduct)
