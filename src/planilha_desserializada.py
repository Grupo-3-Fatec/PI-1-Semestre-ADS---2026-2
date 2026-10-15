import pandas as pd

df = pd.read_csv('data_tratada.csv', sep=';')

def df_dess(Dataframe:df):
    Dataframe = Dataframe.replace(True, "SIM").replace(False, "NÃO")
    Valores = ['ValorContrato', 'ValorParcela', 'ValorTroco']
    Dataframe[Valores] = df[Valores].astype(str)

    return Dataframe

teste = df_dess(df)
print(teste)
