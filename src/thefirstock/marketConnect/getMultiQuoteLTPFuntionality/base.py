from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockGetMultiQuoteLTP(self, dataToken):
        """
        :return:
        """
        pass
