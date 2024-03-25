from thefirstock.ordersNReport.productConversionFunctionality.execution import *


def firstock_ConvertProduct(exchange, tradingSymbol, quantity, product, previousProduct, transactionType, positionType, userId):
    try:

        convertProduct = FirstockConvertProduct(
            exch=exchange,
            tsym=tradingSymbol,
            qty=quantity,
            prd=product,
            prevprd=previousProduct,
            trantype=transactionType,
            postype=positionType,
            userId=userId
        ).firstockConvertProduct()

        return convertProduct

    except Exception as e:
        print(e)
