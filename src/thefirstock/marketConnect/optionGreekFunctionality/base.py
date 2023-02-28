from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockOptionGreek(self, expiryDate, strikePrice, spotPrice, initRate, volatility, optionType):
        """
        :return:
        """
        pass
