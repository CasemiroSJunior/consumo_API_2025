from ApiConsumeCreator import ApiCreator
from StarWars import StarWars

class StarWarsCreator(ApiCreator):
    def create_api_consumer(self) -> StarWars:
        return StarWars()