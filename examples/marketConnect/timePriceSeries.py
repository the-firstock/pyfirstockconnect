from thefirstock import thefirstock

timePriceSeries = thefirstock.firstock_TimePriceSeries(
    exchange="NSE",
    token="22",
    startTime="16/08/2022 09:45:32",
    endTime="15/02/2023 13:45:32",
    interval="5"

)
print(timePriceSeries)
