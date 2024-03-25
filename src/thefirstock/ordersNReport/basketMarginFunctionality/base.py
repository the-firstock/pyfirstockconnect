from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockBasketMargin(self, basket, userId):
        """
        :return:
        """
        pass
