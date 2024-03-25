from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetIndexList(self, exch, userId):
        """
        :return:
        """
        pass
