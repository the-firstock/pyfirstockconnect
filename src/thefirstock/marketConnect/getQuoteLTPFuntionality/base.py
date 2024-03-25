from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetQuoteLTP(self, exch, token, userId):
        """
        :return:
        """
        pass
