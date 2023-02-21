from thefirstock import thefirstock

spanCalculator = thefirstock.firstock_SpanCalculator(
    dataList=[
            {
                "exchange": "NFO",
                "instrumentName": "",
                "symbolName": "NIFTY",
                "expireDate": "23-FEB-2023",
                "optionType": "CE",
                "strikePrice": "17000",
                "netQuantity": "50"
            },
            {
                "exchange": "NFO",
                "instrumentName": "",
                "symbolName": "BANKNIFTY",
                "expireDate": "23-FEB-2023",
                "optionType": "PE",
                "strikePrice": "40000",
                "netQuantity": "-25"
            }
        ]
    )
print(spanCalculator)
