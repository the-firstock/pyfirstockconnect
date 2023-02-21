from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockLogin(self, uid, pwd, factor2, vc, appkey):
        """
        :return:
        """
        pass
