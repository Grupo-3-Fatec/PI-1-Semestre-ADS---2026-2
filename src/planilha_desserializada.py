import pandas as pd
#ValorContrato ValorParcela ValorTroco

df = pd.read_csv('data_tratada.csv', sep=';')
df = pd.DataFrame(df)

def df_formatado(Dataframe):
    Dataframe = df
    Dataframe = df.replace(True, "SIM").replace(False, "NÃO")
    return Dataframe

print(df_formatado(df))