from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockPlaceOrder(self, exch, tsym, qty, prc, prd, trantype, prctyp, ret, trgprc, remarks):
        """
        :return:
        """
        pass
