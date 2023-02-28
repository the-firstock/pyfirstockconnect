from abc import ABC, abstractmethod


class FirstockAPI(ABC):
    @abstractmethod
    def firstockUserDetails(self):
        """
        :return:
        """
        pass
