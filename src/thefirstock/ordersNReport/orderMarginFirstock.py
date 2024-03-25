from thefirstock.ordersNReport.orderMarginFunctionality.execution import *


def firstock_orderMargin(exchange, tradingSymbol, quantity, price, product, transactionType, priceType, userId):
    try:
        orderMargin = FirstockGetOrderMargin(
            exch=exchange,
            tsym=tradingSymbol,
            qty=quantity,
            prc=price,
            prd=product,
            trantype=transactionType,
            prctyp=priceType,
            userId=userId
        ).firstockGetOrderMargin()

        return orderMargin

    except Exception as e:
        print(e)
