#==== Importa a biblioteca pandas e o motor para o excel===#
import pandas as pd

#== CRIA UM DATAFRAME COM O ARQUIVO CSV SERIALIZADO ==#
df = pd.read_csv('data/data_tratada.csv')

def salvar_dataframe_excel(Dataframe, nome_arquivo):
    #== Desserializa os dados da planilha e devolve em um arquivo excel ==#
    
    #== Verifica se o dataframe não é vazio ==#
    if Dataframe is None or Dataframe.empty:
        #ADICIONAR MENSAGEM DE ERRO NO TELEGRAM
        return None
    
    
    #=== Transforma dados que estão em True/False para SIM e NÃO ===#
    Dataframe = Dataframe.replace(True, "SIM").replace(False, "NÃO")
    
    #== Variavel com as colunas tipo float/int/string ==#
    Valores = ['ValorContrato', 'ValorParcela', 'ValorTroco',
               'TaxaPorc', 'TaxaCET']
    #== Variavel com as colunas que são strings ==#
    Colunas_Str = ['Atendente', 'Cliente', 'PropostaTipo', 'PropostaStatus',
                    'BancoDigitado', 'BancoPortado', 'OrigemCaptacao', 'Orgao']
    
    #== Garante que todas as colunas com texto são strings ==#
    Dataframe[Colunas_Str] = Dataframe[Colunas_Str].astype(str)
    
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
    # "#F2F0EF" Coloca cor cinza em todas as linhas
    
    zebrado.iloc[1::2, :] = "background-color: #d8bfd8"
    # "#d8bfd8" muda a cor da linha para lilas a cada 2 linhas
    
    #== | Aplica o estilo ao dataframe | ==#
    Dataframe = Dataframe.style.apply(lambda _:zebrado, axis=None)

    #==== | Caminho | ====#
    caminho = f"data/{nome_arquivo}"

    #== sep=';' (Delimitação de Colunas) ==#
    #== encoding='utf-8-sig' (Para reconhecer acentuação) ==#
    
    Dataframe.to_excel(caminho, encoding='utf-8-sig', sep=';', index=False)
    #ADICIONAR MENSAGEM AO TELEGRAM RETORNANDO A PLANILHA
    return caminho


teste = salvar_dataframe_excel(df,"teste.xlsx")
print(teste)
