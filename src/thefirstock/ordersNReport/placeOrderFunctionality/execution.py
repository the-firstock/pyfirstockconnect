from thefirstock.ordersNReport.placeOrderFunctionality.functions import *


class FirstockPlaceOrder:
    def __init__(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks, userId):
        self.placeOrder = ApiRequests()
        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prc = prc
        self.prd = prd
        self.trantype = trantype
        self.prctyp = prctyp
        self.ret = ret
        self.trgprc = trgprc
        self.remarks = remarks
        self.userId = userId

    def firstockPlaceOrder(self):
        result = self.placeOrder.firstockPlaceOrder(self.exch, self.tsym, self.qty, self.prc, self.prd,
                                                    self.trantype, self.prctyp, self.ret, self.trgprc, self.remarks, self.userId)
        return result
