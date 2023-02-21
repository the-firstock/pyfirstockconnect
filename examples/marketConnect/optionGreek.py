from thefirstock import thefirstock

optionGreek = thefirstock.firstock_OptionGreek(
    expiryDate='23-FEB-2023',
    strikePrice='39000',
    spotPrice='38850',
    initRate='7',
    volatility='20',
    optionType='PE',
)
print(optionGreek)
