from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetOptionChain(self, tsym, exch, strprc, cnt):
        """
        :return:
        """
        pass
