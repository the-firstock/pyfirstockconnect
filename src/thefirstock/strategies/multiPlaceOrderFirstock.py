from thefirstock.strategies.multiPlaceOrder import *


def firstock_MultiPlaceOrder(dataList: list, userId:str):
    try:
        MPL = firstock_multi_placeOrder(
            dataList=dataList,
            userId=userId
        )

        return MPL

    except Exception as e:
        print(e)
