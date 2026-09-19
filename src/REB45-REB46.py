import pandas as pd

def salvar_dataframe_csv(df_filtrado_pelo_lucas, nome_arquivo="relatorio_final.csv"):
    """
    Recebe os dados já limpos e filtrados pelo Lucas 
    e gera o arquivo CSV pronto para abrir no Excel.
    """ 
    if df_filtrado_pelo_lucas is None or df_filtrado_pelo_lucas.empty:
        print("Aviso: DataFrame vazio.")
        return None

    # Adiciona 'data/' na frente do nome do arquivo
    caminho = f"data/{nome_arquivo}"

    # - sep=';' (para o Excel do Brasil entender as colunas)
    # - encoding='utf-8-sig' (para os acentos não ficarem bugados)
    df_filtrado_pelo_lucas.to_csv(caminho, index=False, sep=';', encoding='utf-8-sig')
    print(f"Sucesso! Salvo em: {caminho}")
    
    return caminho

# Teste local
if __name__ == "__main__":
    dados_teste = pd.DataFrame({
        'Atendente': ['ALINE', 'CARLOS'],
        'Valor': [1000, 2000]
    })
    
    # Vai salvar direto em: data/relatorio_final.csv
    salvar_dataframe_csv(dados_teste, "relatorio_final.csv")

#A função poderá ser chamada a quantiade de vezes que for precisado, independente da quantidade de perguntas que vamos responder no telegram
#Exemplo de chamada de função para 4 DFs:

#salvar_dataframe_csv(df_pergunta_1, "data/pergunta_01.csv")
#salvar_dataframe_csv(df_pergunta_2, "data/pergunta_02.csv")
#salvar_dataframe_csv(df_pergunta_3, "data/pergunta_03.csv")
#salvar_dataframe_csv(df_pergunta_4, "data/pergunta_04.csv")

#basicamente a sintaxe para chamar a função será: salvar_dataframe_csv("o nome da darivel que esta o dataframe", "nome da planilha.csv")