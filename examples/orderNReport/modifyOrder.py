from thefirstock import thefirstock

modifyOrder = thefirstock.firstock_ModifyOrder(
    orderNumber="",
    quantity="1",
    price="301",
    triggerPrice="301",
    exchange="NSE",
    tradingSymbol="ITC-EQ",
    priceType="LMT"
)
print(modifyOrder)
