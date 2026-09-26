import pandas as pd

def salvar_dataframe_csv(df_tratada, nome_arquivo):
    """
    Recebe os dados tratados
    Retorna o arquivo CSV.
    """
    #Verifica se o dataframe não é vazio
    if df_tratada is None or df_tratada.empty:
        #ADICIONAR MENSAGEM DE ERRO NO TELEGRAM
        return None

    # Adiciona 'data/' na frente do nome do arquivo
    caminho = f"data/{nome_arquivo}"

    # - sep=';' (Delimitação de Colunas)
    # - encoding='utf-8-sig' (Para reconhecer acentuação)
    df_tratada.to_csv(caminho, index=False, sep=';', encoding='utf-8-sig')
    #ADICIONAR MENSAGEM AO TELEGRAM RETORNANDO A PLANILHA
    return caminho

# Teste local
'''if __name__ == "__main__":
    dados_teste = pd.DataFrame({
        'Atendente': ['ALINE', 'CARLOS'],
        'Valor': [1000, 2000]
    })
    
    # Vai salvar direto em: data/relatorio_final.csv
    salvar_dataframe_csv(dados_teste, "relatorio_final.csv")
'''
#A função poderá ser chamada a quantiade de vezes que for nescessário, independente da
# quantidade de perguntas que vamos responder no telegram
#Exemplo de chamada de função para 3 DFs:

#salvar_dataframe_csv(df_pergunta_1, "data/pergunta_01.csv")
#salvar_dataframe_csv(df_pergunta_2, "data/pergunta_02.csv")
#salvar_dataframe_csv(df_pergunta_3, "data/pergunta_03.csv")

#Syntaxe de execução da função: salvar_dataframe_csv
# ("o nome da variável que esta o dataframe", "nome da planilha.csv")
