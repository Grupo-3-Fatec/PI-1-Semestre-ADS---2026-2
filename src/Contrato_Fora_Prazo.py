import os
import pandas as pd
from datetime import datetime
from tratamento_de_dados import tratamento
from Return_Tabela import salvar_dataframe_csv

def filtrar_contratos_atrasados(df, dias_limite):

    # Define a data de referência baseada na data máxima do arquivo
    data_referencia = df['DataUltimoStatus'].max()
    
    # Calcula quantos dias passaram desde o último status
    df['DiasPassados'] = (data_referencia - df['DataUltimoStatus']).dt.days
    
    # Filtra os contratos que passam de 15 dias
    df_filtrado = df[df['DiasPassados'] > dias_limite].copy()
    
    # Seleciona apenas as informações principais para o relatório
    colunas_principais = [
        'NumeroProposta', 'Cliente', 'CPF', 'Telefone', 
        'PropostaStatus', 'ValorContrato', 'DataUltimoStatus', 'DiasPassados'
    ]
    
    colunas_existentes = [col for col in colunas_principais if col in df_filtrado.columns]
    df_relatorio = df_filtrado[colunas_existentes]
    
    # Salva o resultado em um csv

    
    print(f"Relatório gerado com sucesso! {len(df_relatorio)} contratos encontrados com mais de {dias_limite} dias.")
    return df_relatorio

if __name__ == "__main__":
    filtrar_contratos_atrasados(tratamento(), 15)
