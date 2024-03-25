from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockSpanCalculator(self, dataList, userId):
        """
        :return:
        """
        pass
