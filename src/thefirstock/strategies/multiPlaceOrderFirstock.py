from thefirstock.strategies.multiPlaceOrder import *


def firstock_MultiPlaceOrder(dataList: list):
    try:
        MPL = firstock_multi_placeOrder(
            dataList=dataList
        )

        return MPL

    except Exception as e:
        print(e)
