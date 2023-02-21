from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockTradeBook(self):
        """
        :return:
        """
        pass
