# consumo_API_2025

Este repositório foi criado com base na atividade avaliativa do professor [Orlando Saraiva Junior](https://github.com/orlandosaraivajr) da 1ª [Avaliação de Programação Web 3](https://github.com/orlandosaraivajr/FATEC_2025_1SEM_DW3/tree/main/avaliacao1).

O desafio envolvia o consumo de APIs utilizando a linguagem Python e a biblioteca `requests`, com foco no uso do padrão de projeto *Strategy*. Este padrão permite a criação de diferentes comportamentos (algoritmos) para o consumo de APIs, tornando o código mais modular e fácil de expandir, sem grandes modificações no código principal.

## Objetivo

O objetivo deste projeto é consumir diferentes APIs (Pokemon, Rick and Morty, Star Wars e Crônicas do Gelo e do Fogo), implementando um código organizado que permita a fácil adição de novas APIs sem afetar as partes já implementadas do sistema.

## Requisitos

### Os requisitos da atividade eram:
- Criar um repositório próprio para a atividade, nomeado como **consumo_API_2025**.
- Criar um ambiente virtual Python.
- Instalar a biblioteca `requests` dentro do ambiente virtual utilizando o `pip`.

### Passos de Implementação

1. **Primeiro Commit:**
   - Criar um repositório Git e adicionar os códigos de exemplo fornecidos (main.py e API.py).
   - Realizar o primeiro commit.
   - Configurar o ambiente virtual e instalar a biblioteca `requests` com o comando:
     ```bash
     pip install requests
     ```

2. **Segundo Commit:**
   - Implementar o método `extract(self, id)` na classe `API_Rick_Morty`. O objetivo é:
     - Concatenar o ID com a URL base para formar o endpoint correto.
     - Realizar uma requisição GET para obter dados no formato JSON.
     - Retornar uma tupla com o ID, nome e espécie do personagem.
     - Tratar exceções para evitar que o programa quebre em caso de falha na requisição.

3. **Terceiro Commit:**
   - Implementar o método `extract(self, id)` na classe `API_Star_Wars`. O objetivo é:
     - Concatenar o ID com a URL base para formar o endpoint correto.
     - Realizar uma requisição GET para obter os dados no formato JSON.
     - Retornar uma tupla contendo o nome do personagem e os filmes em que ele aparece.
     - Tratar exceções para garantir a estabilidade do código.

4. **Quarto Commit:**
   - Implementar o método `extract(self, id)` na classe `API_Ice_and_Fire`. O objetivo é:
     - Concatenar o ID com a URL base para formar o endpoint correto.
     - Realizar uma requisição GET para obter os dados no formato JSON.
     - Retornar uma tupla contendo o nome do personagem e as temporadas nas quais ele aparece.
     - Tratar exceções para garantir que o programa não quebre.

5. **Quinto Commit:**
   - Descomentar o trecho de código entre as linhas 19 e 31 no `main.py` e verificar se a saída no terminal corresponde ao modelo esperado (veja o exemplo de saída no início deste README).
   - Criar o arquivo `requirements.txt` com as bibliotecas utilizadas.
   - Adicionar as instruções de execução do projeto no `README.md`.
   - Realizar o último commit.

Ao final, ao rodar o arquivo `main.py`, a saída no terminal deve ser similar à seguinte:

```console
Consumo da API Pokemon
****************************************
(1, 'bulbasaur')
(2, 'ivysaur')

Consumo da API Rick and Morty
****************************************
(1, 'Rick Sanchez', 'Human')
(2, 'Morty Smith', 'Human')

Consumo da API Star Wars
****************************************
('Luke Skywalker', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/6/'])
('C-3PO', ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/', 'https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'])

Consumo da API Crônicas do Gelo e do Fogo
****************************************
('Jon Snow', ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', 'Season 6'])
('Walder', ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 6'])
```

## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/consumo_API_2025.git
   ```

2. Crie um ambiente virtual Python e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Para sistemas Unix (Linux/macOS)
   venv\Scripts\activate      # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o código:
   ```bash
   python main.py
   ```

## Arquivos Importantes

- **main.py**: Arquivo principal que executa o código e consome as APIs.
- **API.py**: Contém as classes responsáveis pelo consumo de APIs, cada uma representando uma API distinta (Pokemon, Rick and Morty, Star Wars, Crônicas do Gelo e do Fogo).
- **requirements.txt**: Lista de dependências necessárias para o funcionamento do projeto.

## Conclusão

Este projeto foi uma ótima oportunidade para aprender sobre consumo de APIs em Python, além de praticar conceitos importantes como o padrão de projeto *Strategy*, que torna o código mais flexível e fácil de manter. A realização da atividade também me ajudou a aprimorar habilidades em tratamento de exceções e no uso de ambientes virtuais para gerenciar dependências de projetos Python.