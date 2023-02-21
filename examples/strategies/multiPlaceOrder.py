from thefirstock import thefirstock

MPL = thefirstock.firstock_MultiPlaceOrder(
    dataList=[
        {
            "exchange": "NSE",
            "tradingSymbol": "ITC-EQ",
            "quantity": "1",
            "price": "0",
            "product": "I",
            "transactionType": "S",
            "priceType": "MKT",
            "retention": "DAY",
            "triggerPrice": "",
            "remarks": ""
        },
        {
            "exchange": "NSE",
            "tradingSymbol": "ITC-EQ",
            "quantity": "1",
            "price": "0",
            "product": "I",
            "transactionType": "S",
            "priceType": "MKT",
            "retention": "DAY",
            "triggerPrice": "",
            "remarks": "Test2"
        },
        {
            "exchange": "NSE",
            "tradingSymbol": "ITC-EQ",
            "quantity": "1",
            "price": "0",
            "product": "I",
            "transactionType": "S",
            "priceType": "MKT",
            "retention": "DAY",
            "triggerPrice": "",
            "remarks": "Test3"
        },
        {
            "exchange": "NSE",
            "tradingSymbol": "ITC-EQ",
            "quantity": "1",
            "price": "0",
            "product": "I",
            "transactionType": "S",
            "priceType": "MKT",
            "retention": "DAY",
            "triggerPrice": "",
            "remarks": "Test1"
        }
    ]
)

print(MPL)
