from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockOrderBook(self):
        """
        :return:
        """
        pass
