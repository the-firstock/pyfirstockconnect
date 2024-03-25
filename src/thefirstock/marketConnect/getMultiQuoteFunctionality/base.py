from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetMultiQuote(self, dataToken, userId):
        """
        :return:
        """
        pass
