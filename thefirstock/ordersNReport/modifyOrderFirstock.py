from thefirstock.ordersNReport.modifyOrderFunctionality.execution import *


def firstock_ModifyOrder(quantity, orderNumber, triggerPrice, price, exchange, tradingSymbol, priceType):
    try:

        modifyOrder = FirstockModifyOrder(
            qty=quantity,
            orderNumber=orderNumber,
            trgprc=triggerPrice,
            prc=price,
            exchange=exchange,
            tradingSymbol=tradingSymbol,
            priceType=priceType
        ).firstockModifyOrder()

        return modifyOrder

    except Exception as e:
        print(e)
