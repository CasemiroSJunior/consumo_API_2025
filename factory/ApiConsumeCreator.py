from abc import ABCMeta, abstractmethod
from factory import iApiConsumer


class ApiCreator(metaclass=ABCMeta):
    @abstractmethod
    def create_api_consumer(self) -> iApiConsumer:
        pass

    def execute(self, id):
        api_consumer = self.create_api_consumer()
        api_consumer.extract(id)
        return api_consumer.get_data()

