from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockLimits(self, userId):
        """
        :return:
        """
        pass