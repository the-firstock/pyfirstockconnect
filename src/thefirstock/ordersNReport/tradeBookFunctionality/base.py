from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockTradeBook(self, userId):
        """
        :return:
        """
        pass
