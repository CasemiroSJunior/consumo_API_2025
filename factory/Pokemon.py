import requests
from iApiConsumer import API_consumer

class Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'
        self.__Data = []

    def extract(self, id):
        URL = self.__URL + str(id)
        try:
            request = requests.get(URL).json()
            self.__Data = (request)
        except request.exceptions.ConnectionError:
            raise ConnectionError("Erro de conexão. Verifique sua internet.")

        except request.exceptions.HTTPError as err:
            raise RuntimeError(f"Erro HTTP: {err}")

        except ValueError as err:
            raise RuntimeError(f"Erro nos dados recebidos: {err}")

        except Exception as err:
            raise RuntimeError(f"Erro inesperado: {err}")

    def get_data(self):
        data = self.__Data
        return ((data.get('id'), data.get('name')))