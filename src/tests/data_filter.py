#importando o pandas
import pandas as pd
#importando tipagem generica
import typing as Any

#definição do DataFrame com base no arquivo csv
df = pd.read_csv('../../data/data.csv', delimiter=";")

#criando a função generica que aceita collumn apenas como string,
#value como qualquer valor e retorna um DataFrame
def singleDataFilter(collumn: str, value: Any) -> pd.DataFrame:

    #filtra as linhas que batem com a requisição.
    #dentro de "filter" vai conter apenas as linhas em boolean
    filter = df[collumn] == value

    #pega as linhas que estao como True e devolve os valores
    response = df[filter]

    return response

multipleDataFilter()







#teste de fato. nao sera considerado no codigo final!!!
print('Vamos buscar dados na tabela!')
collumn = input('Digite o nome da coluna: ')
value = input('Digite o valor a ser filtrado: ')

response = singleDataFilter(collumn, value)

response.to_csv('resultado.csv')
