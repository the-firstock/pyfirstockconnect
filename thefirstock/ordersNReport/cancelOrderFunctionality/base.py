from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockCancelOrder(self, orderNumber):
        """
        :return:
        """
        pass
