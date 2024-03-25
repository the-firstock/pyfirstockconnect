from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockCancelOrder(self, orderNumber, userId):
        """
        :return:
        """
        pass
