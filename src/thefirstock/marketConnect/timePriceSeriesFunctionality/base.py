from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockTimePriceSeries(self, exch, token, st, et, intrv):
        """
        :return:
        """
        pass
