from abc import ABC, abstractmethod

class Index(ABC):
    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def insertKey(self):
        pass
