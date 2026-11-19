#==== Importa a biblioteca pandas e o motor para o excel===#
import pandas as pd

def df_dess(Dataframe):
    #== Desserializa os dados da planilha e devolve em um arquivo excel ==#  
    #=== Transforma dados que estão em True/False para SIM e NÃO ===#
    Dataframe = Dataframe.replace(True, "SIM").replace(False, "NÃO")
    
    #== Variavel com as colunas tipo float/int/string ==#
    Valores = ['ValorContrato', 'ValorParcela', 'ValorTroco',
               'TaxaPorc', 'TaxaCET']
    #== Variavel com as colunas que são strings ==#
    Colunas_Str = ['Atendente', 'Cliente', 'PropostaTipo', 'PropostaStatus',
                    'BancoDigitado', 'BancoPortado', 'OrigemCaptacao', 'Orgao']
    
    #== Vê quais dessas colunas tem no dataframe e filtra a lista ==#
    Valores = [col for col in Valores if col in Dataframe.columns]
    Colunas_Str = [col for col in Colunas_Str if col in Dataframe.columns]
    
    #== Garante que todas as colunas com texto são strings ==#
    Dataframe[Colunas_Str] = Dataframe[Colunas_Str].astype(str)
    
    #== Separa os valores em 2 categorias, Reais e Porcentagem ==#
    ValoresR = ['ValorContrato', 'ValorParcela', 'ValorTroco']
    ValoresP = ['TaxaPorc', 'TaxaCET']

    #== Vê quais dessas colunas tem no dataframe e filtra a lista ==#
    ValoresR = [col for col in ValoresR if col in Dataframe.columns]
    ValoresP = [col for col in ValoresP if col in Dataframe.columns]
        
    #== Transforma as colunas em string e muda '.' para ',' ==#
    Dataframe[Valores] = Dataframe[Valores].astype(str)
    Dataframe[Valores] = Dataframe[Valores].replace(r'\.', ',', regex=True)

    #=== Adiciona R$ na frente do texto em cada linha ===#
    Dataframe[ValoresR] = 'R$' + ' ' + Dataframe[ValoresR]
    #=== Adiciona % no final do texto em cada linha ===#
    Dataframe[ValoresP] = Dataframe[ValoresP] + '%'

    return Dataframe

"""
if __name__ == "__main__":

#== CRIA UM DATAFRAME COM O ARQUIVO CSV SERIALIZADO ==#
    df = pd.read_csv('data/data_tratada.csv', sep = ';')

    teste = df_dess(df)
    print(teste)
"""
