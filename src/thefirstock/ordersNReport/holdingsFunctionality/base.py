from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockHoldings(self):
        """
        :return:
        """
        pass
