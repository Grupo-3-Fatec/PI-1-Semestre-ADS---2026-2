import os
import pandas as pd
from datetime import datetime

def filtrar_contratos_atrasados(dias_limite=15):
    # Sobe um nível para a raiz do projeto
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    raiz_projeto = os.path.dirname(diretorio_atual)
    
    # Caminho correto até o CSV original
    caminho_csv = os.path.join(raiz_projeto, 'data', 'data_tratada.csv')
    
    # Carrega o CSV usando ponto e vírgula como separador
    df = pd.read_csv(caminho_csv, sep=';')
    
    # Converte a coluna de data para o formato datetime
    df['DataUltimoStatus'] = pd.to_datetime(df['DataUltimoStatus'], errors='coerce')
    
    # Define a data de referência baseada na data máxima do arquivo
    data_referencia = df['DataUltimoStatus'].max()
    
    # Calcula quantos dias passaram desde o último status
    df['DiasPassados'] = (data_referencia - df['DataUltimoStatus']).dt.days
    
    # Filtra os contratos que passam de X dias (ex: 15 dias)
    df_filtrado = df[df['DiasPassados'] > dias_limite].copy()
    
    # Seleciona apenas as informações principais para o relatório
    colunas_principais = [
        'NumeroProposta', 'Cliente', 'CPF', 'Telefone', 
        'PropostaStatus', 'ValorContrato', 'DataUltimoStatus', 'DiasPassados'
    ]
    
    colunas_existentes = [col for col in colunas_principais if col in df_filtrado.columns]
    df_relatorio = df_filtrado[colunas_existentes]
    
    # Salva o resultado diretamente na pasta 'data' como CSV
    caminho_saida_csv = os.path.join(raiz_projeto, 'data', 'alerta_prazos.csv')
    df_relatorio.to_csv(caminho_saida_csv, index=False, sep=';', encoding='utf-8-sig')
    
    print(f"Relatório gerado com sucesso! {len(df_relatorio)} contratos encontrados com mais de {dias_limite} dias.")
    print(f"Salvo em: {caminho_saida_csv}")
    return caminho_saida_csv

# Teste
if __name__ == "__main__": 
    filtrar_contratos_atrasados(dias_limite=15)