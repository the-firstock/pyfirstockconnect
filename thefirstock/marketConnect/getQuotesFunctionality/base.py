from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetQuotes(self, exch, token):
        """
        :return:
        """
        pass
