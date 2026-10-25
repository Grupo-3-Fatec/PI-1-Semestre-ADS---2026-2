#==== Importa a biblioteca pandas e o motor para o excel===#
import pandas as pd


def df_dess(Dataframe):
    #== Desserializa os dados da planilha ==#
    
    #=== Transforma dados que estão em True/False para SIM e NÃO ===#
    Dataframe = Dataframe.replace(True, "SIM").replace(False, "NÃO")
    
    #== Variavel com as colunas tipo float ==#
    Valores = ['ValorContrato', 'ValorParcela', 'ValorTroco',
               'TaxaPorc', 'TaxaCET']
    
    #== Separa os valores em 2 categorias, Reais e Porcentagem ==#
    ValoresR = ['ValorContrato', 'ValorParcela', 'ValorTroco']
    ValoresP = ['TaxaPorc', 'TaxaCET']

    #== Transforma as colunas em string e muda '.' para ',' ==#
    Dataframe[Valores] = Dataframe[Valores].astype(str)
    Dataframe[Valores] = Dataframe[Valores].replace(r'\.', ',', regex=True)

    #=== Adiciona R$ na frente do texto em cada linha ===#
    Dataframe[ValoresR] = 'R$' + ' ' + Dataframe[ValoresR]
    #=== Adiciona % no final do texto em cada linha ===#
    Dataframe[ValoresP] = Dataframe[ValoresP] + '%'

    #===== | ESTILIZAÇÃO | =====#
    zebrado = pd.DataFrame("background-color: #F2F0EF",
                           index=Dataframe.index, columns=Dataframe.columns)
    
    zebrado.iloc[1::2, :] = "background-color: #d8bfd8"
    
    return Dataframe.style.apply(lambda _:zebrado, axis=None)

if __name__ == '__main__':
    #== CRIA UM DATAFRAME COM O ARQUIVO CSV SERIALIZADO ==#
    df = pd.read_csv('data_tratada.csv', sep=';')
    teste = df_dess(df)
    teste.to_excel("Data.xlsx", index=False)
    print(teste)
