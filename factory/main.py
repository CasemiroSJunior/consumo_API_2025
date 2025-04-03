from factory.RickAndMortyCreator import RickAndMortyCreator

app = RickAndMortyCreator()
data = app.execute(1)  # Busca o personagem de ID 1
print(data)
