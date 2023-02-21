from thefirstock.ordersNReport.placeOrderFunctionality.execution import *


def firstock_placeOrder(exchange, tradingSymbol, quantity, price, product, transactionType,
                        priceType, retention, triggerPrice, remarks):
    try:
        placeOrder = FirstockPlaceOrder(
            exch=exchange,
            tsym=tradingSymbol,
            qty=quantity,
            prc=price,
            prd=product,
            trantype=transactionType,
            prctyp=priceType,
            ret=retention,
            trgprc=triggerPrice,
            remarks=remarks
        ).firstockPlaceOrder()

        return placeOrder
    except Exception as e:
        print(e)
