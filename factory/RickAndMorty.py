import requests
import iApiConsumer

class RickAndMorty(iApiConsumer.API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'
        self.__Data = []

    def extract(self, id):
        URL = self.__URL + str(id)
        try:
            request = requests.get(URL).json()
            self.__Data = (request)

        except:
            RuntimeError("Não foi possível encontrar o personagem", )

    def get_data(self):
        data = self.__Data
        return ((data.get('id'), data.get('name'), data.get('species')))