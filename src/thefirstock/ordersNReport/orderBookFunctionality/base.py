from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockOrderBook(self, userId):
        """
        :return:
        """
        pass
