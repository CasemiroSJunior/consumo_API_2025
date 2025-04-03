from factory.ApiConsumeCreator import ApiCreator
from factory.RickAndMorty import RickAndMorty

class RickAndMortyCreator(ApiCreator):
    def create_api_consumer(self) -> RickAndMorty:
        return RickAndMorty()
