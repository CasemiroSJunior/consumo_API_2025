from ApiConsumeCreator import ApiCreator
from RickAndMorty import RickAndMorty

class RickAndMortyCreator(ApiCreator):
    def create_api_consumer(self) -> RickAndMorty:
        return RickAndMorty()
