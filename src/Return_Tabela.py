#==== Importa a biblioteca pandas e o motor para o excel===#
import pandas as pd
from planilha_desserializada import df_dess

#== CRIA UM DATAFRAME COM O ARQUIVO CSV SERIALIZADO ==#
df = pd.read_csv('data/data_tratada.csv', sep = ';')

def salvar_dataframe_csv(Dataframe, nome_arquivo):
    #== Devolve planilha em um arquivo excel ==#
    
    #== Aplica a desserialização no dataframe ==#
    Dataframe = df_dess(Dataframe)

    #== Verifica se o dataframe não é vazio ==#
    if Dataframe is None or Dataframe.empty:
        #ADICIONAR MENSAGEM DE ERRO NO TELEGRAM
        return None
    
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
    
    Dataframe.to_excel(caminho, index=False)
    #ADICIONAR MENSAGEM AO TELEGRAM RETORNANDO A PLANILHA
    return caminho

if __name__ == "__main__":
    teste = salvar_dataframe_csv(df,"teste.xlsx")
    print(teste)
