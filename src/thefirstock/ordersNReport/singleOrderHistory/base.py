from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockSingleOrderHistory(self, orderNumber):
        """
        :return:
        """
        pass
