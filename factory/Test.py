from iApiConsumer import API_consumer
from PokemonCreator import PokemonCreator

class ETL:
    def consume(self, id, consumer=PokemonCreator().create_api_consumer() ):
        if issubclass(type(consumer), API_consumer):
            consumer.extract(id)
            print(consumer.get_data())
        else:
            print('Falhou')