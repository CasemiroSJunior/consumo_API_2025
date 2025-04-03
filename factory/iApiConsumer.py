from abc import ABCMeta, abstractmethod

class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass

    @abstractmethod
    def get_data(self):
        pass