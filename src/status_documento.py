"""importa a biblioteca pandas para usar com o csv"""
import pandas as pd
import numpy as np
import tratamento_de_dados as td
def contrato_elegivel(df: pd.DataFrame, condicao: bool):
    """Função que retorna em um dataframe todos os clientes
    que não estão em falta com entrega de documentos"""
    analise = df[['Cliente','NumeroProposta','PossuiGravacao','PossuiFoto']]
    if condicao:
        filtrado = analise[(analise['PossuiFoto'] != False) & (analise['PossuiGravacao'] != False)]
    else:
        filtrado = analise[(analise['PossuiGravacao'] == False) | (analise['PossuiFoto'] == False)]

    return filtrado

if __name__ == "__main__":
    print(contrato_elegivel(td.tratamento(), True))
    print(contrato_elegivel(td.tratamento(), False))
