from abc import ABCMeta, abstractmethod
from iApiConsumer import API_consumer


class ApiCreator(metaclass=ABCMeta):
    @abstractmethod
    def create_api_consumer(self) -> API_consumer:
        pass


    def execute(self, id):
        api_consumer = self.create_api_consumer()
        api_consumer.extract(id)
        return api_consumer.get_data()

