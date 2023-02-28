from thefirstock.ordersNReport.orderMarginFunctionality.functions import *


class FirstockGetOrderMargin:
    def __init__(self, exch, tsym, qty, prc, prd, trantype, prctyp):
        self.getOrderMargin = ApiRequests()

        self.exch = exch
        self.tsym = tsym
        self.qty = qty
        self.prc = prc
        self.prd = prd
        self.trantype = trantype
        self.prctyp = prctyp

    def firstockGetOrderMargin(self):
        result = self.getOrderMargin.firstockGetOrderMargin(self.exch, self.tsym, self.qty, self.prc, self.prd,
                                                            self.trantype, self.prctyp)
        return result
