from thefirstock import thefirstock

getQuotes = thefirstock.firstock_getQuote(
    exchange="NSE",
    token="26000"
)
print(getQuotes)
