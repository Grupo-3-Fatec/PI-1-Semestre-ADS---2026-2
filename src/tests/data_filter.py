#importando o pandas
import pandas as pd
#importando tipagem generica
import typing as Any

#criando a função generica que aceita collumn apenas como string,
#value como qualquer valor e retorna um DataFrame
def singleDataFilter(data_frame: pd.DataFrame, collumn: str, value: Any) -> pd.DataFrame:

    #filtra as linhas que batem com a requisição.
    #dentro de "filter" vai conter apenas as linhas em boolean
    filter = data_frame[collumn] == value

    #pega as linhas que estao como True e devolve os valores
    response = data_frame[filter]

    return response

