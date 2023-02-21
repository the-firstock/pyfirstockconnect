from thefirstock import thefirstock

optionChain = thefirstock.firstock_OptionChain(
            exchange="NFO",
            tradingSymbol="NIFTY23FEB23C18000",
            strikePrice="18000",
            count="5"
            )
print(optionChain)
