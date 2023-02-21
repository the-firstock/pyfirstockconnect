from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockSearchScrips(self, stext):
        """
        :return:
        """
        pass
