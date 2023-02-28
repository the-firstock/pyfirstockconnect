from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetOrderMargin(self, exch, tsym, qty, prc, prd, trantype, prctyp):
        """
        :return:
        """
        pass
