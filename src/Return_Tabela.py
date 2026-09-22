import pandas as pd
import os

def salvar_dataframe_csv(df_tratada, nome_arquivo):
    """
    Recebe os dados tratados
    Retorna o arquivo CSV.
    """
    #Verifica se o dataframe não é vazio
    if df_tratada is None or df_tratada.empty:
        print("Aviso: DataFrame vazio.")
        #ADICIONAR MENSAGEM DE ERRO NO TELEGRAM
        return None

    # Adiciona 'data/' na frente do nome do arquivo
    caminho = f"data/{nome_arquivo}"

    
    #ADICIONAR MENSAGEM AO TELEGRAM RETORNANDO A PLANILHA

    # Descobre o diretório raiz do projeto subindo a pasta 'src'
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    dir_raiz = os.path.dirname(dir_atual)
    
    # Define o caminho completo para a pasta data na raiz
    pasta_data = os.path.join(dir_raiz, "data") 
    os.makedirs(pasta_data, exist_ok=True)
    
    # - sep=';' (Delimitação de Colunas)
    # - encoding='utf-8-sig' (Para reconhecer acentuação)
    caminho = os.path.join(pasta_data, nome_arquivo)
    df_tratada.to_csv(caminho, index=False, sep=';', encoding='utf-8-sig')
     #ADICIONAR MENSAGEM AO TELEGRAM RETORNANDO A PLANILHA
    return caminho




# Teste local - Quando a função for importada, e caso o tete estiver ativo. ele nao vai ser executado
# Ele vai ser executado apenas se o arquivo for executado diretamente (como ao apertar F5 ou rodar pelo terminal).
# Teste local com um DataFrame mais robusto:
#if __name__ == "__main__":
    dados_teste = pd.DataFrame({
        'Atendente': ['ALINE', 'CARLOS', 'BEATRIZ', 'DANIEL', 'ALINE', 'CARLOS', 'BEATRIZ'],
        'Região': ['Norte', 'Sul', 'Leste', 'Oeste', 'Sul', 'Norte', 'Oeste'],
        'Valor': [1500.50, 2300.00, 1200.75, 3400.00, 950.00, 1800.25, 4100.00],
        'Status': ['Concluído', 'Pendente', 'Concluído', 'Concluído', 'Pendente', 'Concluído', 'Pendente']
    })
    
    # Salva o arquivo de teste robusto na pasta data/
    caminho_salvo = salvar_dataframe_csv(dados_teste, "relatorio_teste_local.csv")
    print(f"Arquivo de teste gerado com sucesso em: {caminho_salvo}")





#A função poderá ser chamada a quantiade de vezes que for nescessário, independente da
# quantidade de perguntas que vamos responder no telegram
#Exemplo de chamada de função para 3 DFs:

#Syntaxe de execução da função: salvar_dataframe_csv
# ("o nome da variável que esta o dataframe", "nome da planilha.csv")

#salvar_dataframe_csv(df_pergunta_1, "pergunta_01.csv")
#salvar_dataframe_csv(df_pergunta_2, "pergunta_02.csv")
#salvar_dataframe_csv(df_pergunta_3, "pergunta_03.csv")

