from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockSearchScrips(self, stext, userId):
        """
        :return:
        """
        pass
