from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockSpanCalculator(self, dataList):
        """
        :return:
        """
        pass
