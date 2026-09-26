"""importa a biblioteca pandas para usar com o csv"""
import pandas as pd
# data = pd.read_csv('data.csv', sep=';')
# df_docs = pd.DataFrame(data)

#==========VER CONTRATOS QUE NÃO POSSUEM GRAVAÇÃO==========

def sem_gravacao(df: pd.DataFrame):
    """Função que retorna um dataframe com os clientes
    que não tem gravação com o documento"""

    filtro = (df['PossuiGravacao'] == False)
# filtro  <-  armazena a condição dentro de uma variavel
# ()  <-  oque esta dentro se torna uma condição,
# |  <-  equivalente ao "OR" do python    

    filtrado = df.loc[filtro, ['Cliente', 'NumeroProposta', 'PossuiGravacao']]
    return filtrado

#df_docs.loc <- peço para o dataframe selecionar e indexar as colunas que eu escolher
#[filtro, []] <- "filtro" é a condição, o dataframe ver as linhas que atendem a condição
#[ , [colunas]] <- "colunas" são as colunas que vai ter no dataframe e vão passar pela condição

#==========VER CONTRATOS QUE NÃO POSSUEM FOTO/GRAVAÇÃO==========

def sem_documento(df: pd.DataFrame):
    """Função que retorna um dataframe com os clientes
    que tem qualquer um dos documentos em falta"""

    filtro = ((df['PossuiGravacao'] == False) |
             (df['PossuiFoto'] == False))
#
    filtrado = df.loc[filtro, ['Cliente', 'NumeroProposta', 'PossuiGravacao', 'PossuiFoto']]
    return filtrado

#==========VER CONTRATOS QUE POSSUEM FOTO/GRAVAÇÃO==========

def contrato_elegivel(df: pd.DataFrame):
    """Função que retorna em um dataframe todos os clientes
    que não estão em falta com entrega de documentos"""

    filtro = (df['PossuiGravacao'] == 'SIM') | (df['PossuiFoto'] == 'SIM')
#
    filtrado = df.loc[filtro, ['Cliente', 'NumeroProposta', 'PossuiGravacao', 'PossuiFoto']]
    return filtrado

if __name__ == "__main__":
    pass
    # print(sem_documento())
    # print(sem_gravacao())
    # print(contrato_elegivel())
