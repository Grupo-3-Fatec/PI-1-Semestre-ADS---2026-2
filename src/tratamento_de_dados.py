"""=== IMPORTAÇÂO DE BIBLIOTECAS ==="""

import pandas as pd
import numpy as np

# === LENDO A PLANILHA ===
df_contratos = pd.read_csv(
    'D:/FATEC/1° Semestre/Projeto Integrador/Projeto/CSV/PlanilhaContratosUTF.csv', delimiter=';'
    )
df_tratada = df_contratos

# === TRATAMENTO NOME DE COLUNAS ===
df_tratada = df_tratada.rename(columns={
    ' ValorContrato ': 'ValorContrato', 
    ' ValorParcela ': 'ValorParcela', 
    ' ValorTroco ': 'ValorTroco'})

# === TRATAMENTO DE TIPOS DE DADOS ===

# === TRATAMENTO DE CONVERSÃO PARA VALORES DE DATA ===
df_tratada['DataEnvioCIP'] = pd.to_datetime(
    df_tratada['DataEnvioCIP'], format='%d/%m/%Y'
    )
df_tratada['DataUltimoStatus'] = pd.to_datetime(
    df_tratada['DataUltimoStatus'], format='%d/%m/%Y'
    )
df_tratada['DataCriacaoProposta'] = pd.to_datetime(
    df_tratada['DataCriacaoProposta'], format='%d/%m/%Y'
    )

# === TRATAMENTO DE CONVERSÃO PARA VALORES NUMÉRICOS FLOAT ===

# = TRATAMENTO COLUNA ValorContrato =
df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace('R$', '')
df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace('.', '')
df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace('-', '0')
df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace(' ', '')
df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace(',', '.')
df_tratada['ValorContrato'] = pd.to_numeric(df_tratada['ValorContrato'], downcast='float')

# = TRATAMENTO COLUNA ValorParcela =
df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace('R$', '')
df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace('.', '')
df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace('-', '0')
df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace(' ', '')
df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace(',', '.')
df_tratada['ValorParcela'] = pd.to_numeric(df_tratada['ValorParcela'], downcast='float')

# = TRATAMENTO COLUNA ValorTroco =
df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace('R$', '')
df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace('.', '')
df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace('-', '0')
df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace(' ', '')
df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace(',', '.')
df_tratada['ValorTroco'] = pd.to_numeric(df_tratada['ValorTroco'], downcast='float')

# = TRATAMENTO COLUNA TaxaPorc =
df_tratada['TaxaPorc'] = df_tratada['TaxaPorc'].str.replace(',','.')
df_tratada['TaxaPorc'] = df_tratada['TaxaPorc'].str.replace('%','')
df_tratada['TaxaPorc'] = pd.to_numeric(df_tratada['TaxaPorc'], downcast='float')
df_tratada['TaxaPorc'] = df_tratada['TaxaPorc'] / 100

# = TRATAMENTO COLUNA TaxaCET =
df_tratada['TaxaCET'] = df_tratada['TaxaCET'].str.replace(',','.')
df_tratada['TaxaCET'] = df_tratada['TaxaCET'].str.replace('%','')
df_tratada['TaxaCET'] = pd.to_numeric(df_tratada['TaxaCET'], downcast='float')
df_tratada['TaxaCET'] = df_tratada['TaxaCET'] / 100


# === TRATAMENTO DE STRINGS ===

# = TRATAMENTO COLUNA Atendente =
df_tratada['Atendente'] = df_tratada['Atendente'].str.strip()

# = TRATAMENTO COLUNA Cliente
df_tratada['Cliente'] = df_tratada['Cliente'].str.strip()

# = TRATAMENTO COLUNA CPF =
df_tratada['CPF'] = df_tratada['CPF'].str.strip()

# = TRATAMENTO COLUNA Telefone =
df_tratada['Telefone'] = df_tratada['Telefone'].str.strip()

# = TRATAMENTO COLUNA PropostaTipo =
df_tratada['PropostaTipo'] = df_tratada['PropostaTipo'].str.strip()

# = TRATAMENTO COLUNA PropostaStatus =
df_tratada['PropostaStatus'] = df_tratada['PropostaStatus'].str.strip()

# = TRATAMENTO COLUNA BancoDigitado =
df_tratada['BancoDigitado'] = df_tratada['BancoDigitado'].str.strip()

# = TRATAMENTO COLUNA BancoPortado =
df_tratada['BancoPortado'] = np.where(
    df_tratada['BancoPortado'].isna(), 'NÃO INFORMADO', df_tratada['BancoPortado']
    )
df_tratada['BancoPortado'] = np.where(
    df_tratada['BancoPortado'].isna(), 'NÃO INFORMADO', df_tratada['BancoPortado']
    )

# = TRATAMENTO COLUNA DataSaldoPago =
df_tratada['DataSaldoPago'] = np.where(
    df_tratada['DataSaldoPago'].isna(), 'PAGAMENTO NÃO CONFIRMADO', df_tratada['DataSaldoPago']
    )

# = TRATAMENTO COLUNA OrigemCaptacao =
df_tratada['OrigemCaptacao'] = df_tratada['OrigemCaptacao'].str.strip()

# = TRATAMENTO COLUNA Orgao =
df_tratada['Orgao'] = df_tratada['Orgao'].str.strip()

# = TRATAMENTO COLUNA PossuiGravacao =
df_tratada['PossuiGravacao'] = df_tratada['PossuiGravacao'].str.strip()
df_tratada['PossuiGravacao'] = np.where(df_tratada['PossuiGravacao'] == 'SIM', True, False)

# = TRATAMENTO COLUNA PossuiFoto =
df_tratada['PossuiFoto'] = df_tratada['PossuiFoto'].str.strip()
df_tratada['PossuiFoto'] = np.where(df_tratada['PossuiFoto'] == 'SIM', True, False)

# = TRATAMENTO COLUNA EmRevisao =
df_tratada['EmRevisao'] = df_tratada['EmRevisao'].str.strip()
df_tratada['EmRevisao'] = np.where(df_tratada['EmRevisao'] == 'SIM', True, False)

# = TRATAMENTO COLUNA PossuiPendente =
df_tratada['PossuiPendente'] = df_tratada['PossuiPendente'].str.strip()
df_tratada['PossuiPendente'] = np.where(
    df_tratada['PossuiPendente'] == 'SIM', True, False
    )
