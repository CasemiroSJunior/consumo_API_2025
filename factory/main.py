from PokemonCreator import PokemonCreator
from RickAndMortyCreator import RickAndMortyCreator
from StarWarsCreator import StarWarsCreator
from IceAndFireCreator import IceAndFireCreator
from Test import ETL

API_Pokemon = PokemonCreator().create_api_consumer()
API_Rick_Morty = RickAndMortyCreator().create_api_consumer()
API_Star_Wars = StarWarsCreator().create_api_consumer()
API_Ice_and_Fire = IceAndFireCreator().create_api_consumer()


etl = ETL()
print('\n\nConsumo da API Pokemon')
print(40 * '*')
etl.consume(1, API_Pokemon)
etl.consume(2)
print('\n\nConsumo da API Rick and Morty')
print(40 * '*')
etl.consume(1, API_Rick_Morty)
etl.consume(2, API_Rick_Morty)
print('\n\nConsumo da API Star Wars')
print(40 * '*')
etl.consume(1, API_Star_Wars)
etl.consume(2, API_Star_Wars)
print('\n\nConsumo da API Crônicas do Gelo e do Fogo')
print(40 * '*')
etl.consume(583, API_Ice_and_Fire)
etl.consume(2, API_Ice_and_Fire)