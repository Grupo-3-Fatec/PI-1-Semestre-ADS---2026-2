# === IMPORTAÇÂO DE BIBLIOTECAS ===
import pandas as pd
import numpy as np

def tratamento():
    # === LENDO A PLANILHA ===
    dfContratos = pd.read_csv('D:/FATEC/1° Semestre/Projeto Integrador/Projeto/CSV/PlanilhaContratosUTF.csv', delimiter=';')
    dfTratada = dfContratos

    # === TRATAMENTO NOME DE COLUNAS ===
    dfTratada = dfTratada.rename(
        columns={' ValorContrato ': 'ValorContrato',
                 ' ValorParcela ': 'ValorParcela',
                 ' ValorTroco ': 'ValorTroco'
                })

    # === TRATAMENTO DE DADOS ===

    # = TRATAMENTO COLUNA Atendente =
    dfTratada['Atendente'] = dfTratada['Atendente'].str.strip()
    dfTratada['Atendente'] = dfTratada['Atendente'].str.upper()

    # = TRATAMENTO COLUNA Cliente 
    dfTratada['Cliente'] = dfTratada['Cliente'].str.strip()
    dfTratada['Cliente'] = dfTratada['Cliente'].str.upper()

    # = TRATAMENTO COLUNA CPF =
    dfTratada['CPF'] = dfTratada['CPF'].str.upper()
    dfTratada['CPF'] = dfTratada['CPF'].str.replace(' ', '')
    dfTratada['CPF'] = np.where(dfTratada['CPF'].isna(), 'NÃO INFORMADO', np.where(dfTratada['CPF'].str.contains('[A-z]', regex=True, na=False), 'NÃO INFORMADO CORRETAMENTE', dfTratada['CPF']))
    
    # = TRATAMENTO COLUNA Telefone =
    dfTratada['Telefone'] = dfTratada['Telefone'].str.strip()
    dfTratada['Telefone'] = dfTratada['Telefone'].str.upper()
    dfTratada['Telefone'] = np.where(dfTratada['Telefone'].isna(), 'NÃO INFORMADO', np.where(dfTratada['Telefone'].str.contains('[A-z]', regex=True, na=False), 'NÃO INFORMADO CORRETAMENTE', dfTratada['Telefone']))

    # = TRATAMENTO COLUNA EspecieBeneficio =

    # = TRATAMENTO COLUNA PropostaTipo =
    dfTratada['PropostaTipo'] = dfTratada['PropostaTipo'].str.strip()
    dfTratada['PropostaTipo'] = dfTratada['PropostaTipo'].str.upper()

    # = TRATAMENTO COLUNA NumeroProposta =

    # = TRATAMENTO COLUNA PropostaStatus =
    dfTratada['PropostaStatus'] = dfTratada['PropostaStatus'].str.strip()
    dfTratada['PropostaStatus'] = dfTratada['PropostaStatus'].str.upper()

    # = TRATAMENTO COLUNA BancoDigitado =
    dfTratada['BancoDigitado'] = dfTratada['BancoDigitado'].str.strip()
    dfTratada['BancoDigitado'] = dfTratada['BancoDigitado'].str.upper()

    # = TRATAMENTO COLUNA ValorContrato =
    dfTratada['ValorContrato'] = dfTratada['ValorContrato'].str.upper()
    dfTratada['ValorContrato'] = dfTratada['ValorContrato'].str.replace('R$', '')
    dfTratada['ValorContrato'] = dfTratada['ValorContrato'].str.replace('.', '')
    dfTratada['ValorContrato'] = dfTratada['ValorContrato'].str.replace('-', '0')
    dfTratada['ValorContrato'] = dfTratada['ValorContrato'].str.replace(' ', '')
    dfTratada['ValorContrato'] = dfTratada['ValorContrato'].str.replace(',', '.')
    dfTratada['ValorContrato'] = pd.to_numeric(dfTratada['ValorContrato'], downcast='float')

    # = TRATAMENTO COLUNA ValorParcela =
    dfTratada['ValorParcela'] = dfTratada['ValorParcela'].str.upper()
    dfTratada['ValorParcela'] = dfTratada['ValorParcela'].str.replace('R$', '')
    dfTratada['ValorParcela'] = dfTratada['ValorParcela'].str.replace('.', '')
    dfTratada['ValorParcela'] = dfTratada['ValorParcela'].str.replace('-', '0')
    dfTratada['ValorParcela'] = dfTratada['ValorParcela'].str.replace(' ', '')
    dfTratada['ValorParcela'] = dfTratada['ValorParcela'].str.replace(',', '.')
    dfTratada['ValorParcela'] = pd.to_numeric(dfTratada['ValorParcela'], downcast='float')

    # = TRATAMENTO COLUNA ValorTroco =
    dfTratada['ValorTroco'] = dfTratada['ValorTroco'].str.upper()
    dfTratada['ValorTroco'] = dfTratada['ValorTroco'].str.replace('R$', '')
    dfTratada['ValorTroco'] = dfTratada['ValorTroco'].str.replace('.', '')
    dfTratada['ValorTroco'] = dfTratada['ValorTroco'].str.replace('-', '0')
    dfTratada['ValorTroco'] = dfTratada['ValorTroco'].str.replace(' ', '')
    dfTratada['ValorTroco'] = dfTratada['ValorTroco'].str.replace(',', '.')
    dfTratada['ValorTroco'] = pd.to_numeric(dfTratada['ValorTroco'], downcast='float')

    # = TRATAMENTO COLUNA TaxaPorc =
    dfTratada['TaxaPorc'] = dfTratada['TaxaPorc'].str.replace(',','.')
    dfTratada['TaxaPorc'] = dfTratada['TaxaPorc'].str.replace('%','') 
    dfTratada['TaxaPorc'] = pd.to_numeric(dfTratada['TaxaPorc'], downcast='float')
    dfTratada['TaxaPorc'] = dfTratada['TaxaPorc'] / 100

    # = TRATAMENTO COLUNA TaxaCET = 
    dfTratada['TaxaCET'] = dfTratada['TaxaCET'].str.replace(',','.') 
    dfTratada['TaxaCET'] = dfTratada['TaxaCET'].str.replace('%','') 
    dfTratada['TaxaCET'] = pd.to_numeric(dfTratada['TaxaCET'], downcast='float')
    dfTratada['TaxaCET'] = dfTratada['TaxaCET'] / 100

    # = TRATAMENTO COLUNA QuantidadeParcelas =

    # = TRATAMENTO COLUNA BancoPortado =
    dfTratada['BancoPortado'] = dfTratada['BancoPortado'].str.strip()
    dfTratada['BancoPortado'] = dfTratada['BancoPortado'].str.upper()
    dfTratada['BancoPortado'] = np.where(dfTratada['BancoPortado'].isna(), 'NÃO INFORMADO', dfTratada['BancoPortado'])

    # = TRATAMENTO COLUNA DataEnvioCIP =
    dfTratada['DataEnvioCIP'] = pd.to_datetime(dfTratada['DataEnvioCIP'], format='%d/%m/%Y')

    # = TRATAMENTO COLUNA DataSaldoPago =
    dfTratada['DataSaldoPago'] = np.where(dfTratada['DataSaldoPago'].isna(), 'PORTABILIDADE NÃO CONFIRMADA', dfTratada['DataSaldoPago'])

    # = TRATAMENTO COLUNA OrigemCaptacao =
    dfTratada['OrigemCaptacao'] = dfTratada['OrigemCaptacao'].str.strip()
    dfTratada['OrigemCaptacao'] = dfTratada['OrigemCaptacao'].str.upper()

    # = TRATAMENTO COLUNA Orgao =
    dfTratada['Orgao'] = dfTratada['Orgao'].str.strip()
    dfTratada['Orgao'] = dfTratada['Orgao'].str.upper()

    # = TRATAMENTO COLUNA PossuiGravacao =
    dfTratada['PossuiGravacao'] = dfTratada['PossuiGravacao'].str.strip()
    dfTratada['PossuiGravacao'] = dfTratada['PossuiGravacao'].str.upper()
    dfTratada['PossuiGravacao'] = np.where(dfTratada['PossuiGravacao'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA PossuiFoto =
    dfTratada['PossuiFoto'] = dfTratada['PossuiFoto'].str.strip()
    dfTratada['PossuiFoto'] = dfTratada['PossuiFoto'].str.upper()
    dfTratada['PossuiFoto'] = np.where(dfTratada['PossuiFoto'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA EmRevisao =
    dfTratada['EmRevisao'] = dfTratada['EmRevisao'].str.strip()
    dfTratada['EmRevisao'] = dfTratada['EmRevisao'].str.upper()
    dfTratada['EmRevisao'] = np.where(dfTratada['EmRevisao'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA DataUltimoStatus =
    dfTratada['DataUltimoStatus'] = pd.to_datetime(dfTratada['DataUltimoStatus'], format='%d/%m/%Y')

    # = TRATAMENTO COLUNA PossuiPendente =
    dfTratada['PossuiPendente'] = dfTratada['PossuiPendente'].str.strip()
    dfTratada['PossuiPendente'] = dfTratada['PossuiPendente'].str.upper()
    dfTratada['PossuiPendente'] = np.where(dfTratada['PossuiPendente'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA DataCriacaoProposta =
    dfTratada['DataCriacaoProposta'] = pd.to_datetime(dfTratada['DataCriacaoProposta'], format='%d/%m/%Y')

    # = Retorno da Função =
    return dfTratada
if __name__ == "__main__":
    teste = tratamento()
    print(teste.info())