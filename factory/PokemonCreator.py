from ApiConsumeCreator import ApiCreator
from Pokemon import Pokemon

class PokemonCreator(ApiCreator):
    def create_api_consumer(self) -> Pokemon:
        return Pokemon()
