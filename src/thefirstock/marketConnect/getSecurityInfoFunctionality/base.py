from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetSecurityInfo(self, exch, token, userId):
        """
        :return:
        """
        pass
