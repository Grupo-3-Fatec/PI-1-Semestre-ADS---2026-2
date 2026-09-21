# === IMPORTAÇÂO DE BIBLIOTECAS ===
import pandas as pd
import numpy as np

# === LENDO A PLANILHA ===
df_Contratos = pd.read_csv('D:/FATEC/1° Semestre/Projeto Integrador/Projeto/CSV/PlanilhaContratosUTF.csv', delimiter=';')
df_Tratada = df_Contratos

# === TRATAMENTO NOME DE COLUNAS ===
df_Tratada = df_Tratada.rename(columns={' ValorContrato ': 'ValorContrato', ' ValorParcela ': 'ValorParcela', ' ValorTroco ': 'ValorTroco'})

# === TRATAMENTO DE TIPOS DE DADOS ===

# === TRATAMENTO DE CONVERSÃO PARA VALORES DE DATA ===
df_Tratada['DataEnvioCIP'] = pd.to_datetime(df_Tratada['DataEnvioCIP'], format='%d/%m/%Y')
df_Tratada['DataUltimoStatus'] = pd.to_datetime(df_Tratada['DataUltimoStatus'], format='%d/%m/%Y')
df_Tratada['DataCriacaoProposta'] = pd.to_datetime(df_Tratada['DataCriacaoProposta'], format='%d/%m/%Y')

# === TRATAMENTO DE CONVERSÃO PARA VALORES NUMÉRICOS FLOAT ===

# = TRATAMENTO COLUNA ValorContrato =
df_Tratada['ValorContrato'] = df_Tratada['ValorContrato'].str.replace('R$', '')
df_Tratada['ValorContrato'] = df_Tratada['ValorContrato'].str.replace('.', '')
df_Tratada['ValorContrato'] = df_Tratada['ValorContrato'].str.replace('-', '0')
df_Tratada['ValorContrato'] = df_Tratada['ValorContrato'].str.replace(' ', '')
df_Tratada['ValorContrato'] = df_Tratada['ValorContrato'].str.replace(',', '.')
df_Tratada['ValorContrato'] = pd.to_numeric(df_Tratada['ValorContrato'], downcast='float')

# = TRATAMENTO COLUNA ValorParcela =
df_Tratada['ValorParcela'] = df_Tratada['ValorParcela'].str.replace('R$', '')
df_Tratada['ValorParcela'] = df_Tratada['ValorParcela'].str.replace('.', '')
df_Tratada['ValorParcela'] = df_Tratada['ValorParcela'].str.replace('-', '0')
df_Tratada['ValorParcela'] = df_Tratada['ValorParcela'].str.replace(' ', '')
df_Tratada['ValorParcela'] = df_Tratada['ValorParcela'].str.replace(',', '.')
df_Tratada['ValorParcela'] = pd.to_numeric(df_Tratada['ValorParcela'], downcast='float')

# = TRATAMENTO COLUNA ValorTroco =
df_Tratada['ValorTroco'] = df_Tratada['ValorTroco'].str.replace('R$', '')
df_Tratada['ValorTroco'] = df_Tratada['ValorTroco'].str.replace('.', '')
df_Tratada['ValorTroco'] = df_Tratada['ValorTroco'].str.replace('-', '0')
df_Tratada['ValorTroco'] = df_Tratada['ValorTroco'].str.replace(' ', '')
df_Tratada['ValorTroco'] = df_Tratada['ValorTroco'].str.replace(',', '.')
df_Tratada['ValorTroco'] = pd.to_numeric(df_Tratada['ValorTroco'], downcast='float')

# = TRATAMENTO COLUNA TaxaPorc =
df_Tratada['TaxaPorc'] = df_Tratada['TaxaPorc'].str.replace(',','.') 
df_Tratada['TaxaPorc'] = df_Tratada['TaxaPorc'].str.replace('%','') 
df_Tratada['TaxaPorc'] = pd.to_numeric(df_Tratada['TaxaPorc'], downcast='float')
df_Tratada['TaxaPorc'] = df_Tratada['TaxaPorc'] / 100

# = TRATAMENTO COLUNA TaxaCET = 
df_Tratada['TaxaCET'] = df_Tratada['TaxaCET'].str.replace(',','.') 
df_Tratada['TaxaCET'] = df_Tratada['TaxaCET'].str.replace('%','') 
df_Tratada['TaxaCET'] = pd.to_numeric(df_Tratada['TaxaCET'], downcast='float')
df_Tratada['TaxaCET'] = df_Tratada['TaxaCET'] / 100


# === TRATAMENTO DE STRINGS ===

# = TRATAMENTO COLUNA Atendente =
df_Tratada['Atendente'] = df_Tratada['Atendente'].str.strip()

# = TRATAMENTO COLUNA Cliente 
df_Tratada['Cliente'] = df_Tratada['Cliente'].str.strip()

# = TRATAMENTO COLUNA CPF =
df_Tratada['CPF'] = df_Tratada['CPF'].str.strip()

# = TRATAMENTO COLUNA Telefone =
df_Tratada['Telefone'] = df_Tratada['Telefone'].str.strip()

# = TRATAMENTO COLUNA PropostaTipo =
df_Tratada['PropostaTipo'] = df_Tratada['PropostaTipo'].str.strip()

# = TRATAMENTO COLUNA PropostaStatus =
df_Tratada['PropostaStatus'] = df_Tratada['PropostaStatus'].str.strip()

# = TRATAMENTO COLUNA BancoDigitado =
df_Tratada['BancoDigitado'] = df_Tratada['BancoDigitado'].str.strip()

# = TRATAMENTO COLUNA BancoPortado =
df_Tratada['BancoPortado'] = np.where(df_Tratada['BancoPortado'].isna(), 'NÃO INFORMADO', df_Tratada['BancoPortado'])
df_Tratada['BancoPortado'] = np.where(df_Tratada['BancoPortado'].isna(), 'NÃO INFORMADO', df_Tratada['BancoPortado'])

# = TRATAMENTO COLUNA DataSaldoPago =
df_Tratada['DataSaldoPago'] = np.where(df_Tratada['DataSaldoPago'].isna(), 'PAGAMENTO NÃO CONFIRMADO', df_Tratada['DataSaldoPago'])

# = TRATAMENTO COLUNA OrigemCaptacao =
df_Tratada['OrigemCaptacao'] = df_Tratada['OrigemCaptacao'].str.strip()

# = TRATAMENTO COLUNA Orgao =
df_Tratada['Orgao'] = df_Tratada['Orgao'].str.strip()

# = TRATAMENTO COLUNA PossuiGravacao =
df_Tratada['PossuiGravacao'] = df_Tratada['PossuiGravacao'].str.strip()
df_Tratada['PossuiGravacao'] = np.where(df_Tratada['PossuiGravacao'] == 'SIM', True, False)

# = TRATAMENTO COLUNA PossuiFoto =
df_Tratada['PossuiFoto'] = df_Tratada['PossuiFoto'].str.strip()
df_Tratada['PossuiFoto'] = np.where(df_Tratada['PossuiFoto'] == 'SIM', True, False)

# = TRATAMENTO COLUNA EmRevisao =
df_Tratada['EmRevisao'] = df_Tratada['EmRevisao'].str.strip()
df_Tratada['EmRevisao'] = np.where(df_Tratada['EmRevisao'] == 'SIM', True, False)

# = TRATAMENTO COLUNA PossuiPendente =
df_Tratada['PossuiPendente'] = df_Tratada['PossuiPendente'].str.strip()
df_Tratada['PossuiPendente'] = np.where(df_Tratada['PossuiPendente'] == 'SIM', True, False)