from thefirstock import thefirstock

basketMargin = thefirstock.firstock_BasketMargin(
    basket=[
        {
            "exchange": "NFO",
            "tradingSymbol": "NIFTY23FEB23P17000",
            "quantity": "50",
            "transactionType": "S",
            "price": "0",
            "product": "M",
            "priceType": "LMT"
        },
        {
            "exchange": "NFO",
            "tradingSymbol": "NIFTY23FEB23C19000",
            "quantity": "50",
            "transactionType": "S",
            "price": "0",
            "product": "M",
            "priceType": "LMT"
        },
        {
            "exchange": "NFO",
            "tradingSymbol": "NIFTY23FEB23C19000",
            "quantity": "50",
            "transactionType": "S",
            "price": "0",
            "product": "M",
            "priceType": "LMT"
        }
    ]
)
print(basketMargin)
