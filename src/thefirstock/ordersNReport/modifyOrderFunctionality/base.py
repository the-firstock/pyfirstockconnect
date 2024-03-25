from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockModifyOrder(self, qty, orderNumber, trgprc, prc, exchange, tradingSymbol, priceType, userId):
        """
        :return:
        """
        pass
