from thefirstock.ordersNReport.productConversionFunctionality.functions import *


class FirstockConvertProduct:
    def __init__(self, exch, tsym, qty, prd, prevprd, trantype, postype, userId):
        self.convertProduct = ApiRequests()
        self.userId = userId
        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prd = prd
        self.prevprd = prevprd
        self.trantype = trantype
        self.postype = postype

    def firstockConvertProduct(self):
        result = self.convertProduct.firstockConvertProduct(self.exch, self.tsym, self.qty, self.prd, self.prevprd,
                                                            self.trantype, self.postype, self.userId)
        return result
