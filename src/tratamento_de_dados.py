# === IMPORTAÇÂO DE BIBLIOTECAS ===
import pandas as pd
import numpy as np
import os

def tratamento():
    # === FUNÇÃO PARA LER E TRATAR DADOS DA PLANILHA ===
    # === LENDO A PLANILHA ===
    basedir = os.path.dirname(os.path.dirname(__file__))
    localPlanilha = os.path.join(basedir, 'data')
    df_tratada = pd.read_csv(
        localPlanilha + '\\data.csv',
    delimiter=';'
    )

    # === TRATAMENTO NOME DE COLUNAS ===
    df_tratada = df_tratada.rename(
        columns={' ValorContrato ': 'ValorContrato',
                 ' ValorParcela ': 'ValorParcela',
                 ' ValorTroco ': 'ValorTroco'
                })

    # === TRATAMENTO DE DADOS ===

    # = TRATAMENTO COLUNA Atendente =
    df_tratada['Atendente'] = df_tratada['Atendente'].str.strip()
    df_tratada['Atendente'] = df_tratada['Atendente'].str.upper()

    # = TRATAMENTO COLUNA Cliente =
    df_tratada['Cliente'] = df_tratada['Cliente'].str.strip()
    df_tratada['Cliente'] = df_tratada['Cliente'].str.upper()

    # = TRATAMENTO COLUNA CPF =
    df_tratada['CPF'] = df_tratada['CPF'].str.upper()
    df_tratada['CPF'] = df_tratada['CPF'].str.replace(' ', '')
    df_tratada['CPF'] = np.where(df_tratada['CPF'].isna(),
                        'NÃO INFORMADO',
                        np.where(df_tratada['CPF'].str.contains('[A-z]', regex=True, na=False),
                                 'NÃO INFORMADO CORRETAMENTE',
                                 df_tratada['CPF']))
    
    # = TRATAMENTO COLUNA Telefone =
    df_tratada['Telefone'] = df_tratada['Telefone'].str.strip()
    df_tratada['Telefone'] = df_tratada['Telefone'].str.upper()
    df_tratada['Telefone'] = np.where(df_tratada['Telefone'].isna(),
                             'NÃO INFORMADO',
                             np.where(df_tratada['Telefone'].str.contains('[A-z]', regex=True, na=False),
                                      'NÃO INFORMADO CORRETAMENTE',
                                      df_tratada['Telefone']))

    # = TRATAMENTO COLUNA EspecieBeneficio =

    # = TRATAMENTO COLUNA PropostaTipo =
    df_tratada['PropostaTipo'] = df_tratada['PropostaTipo'].str.strip()
    df_tratada['PropostaTipo'] = df_tratada['PropostaTipo'].str.upper()

    # = TRATAMENTO COLUNA NumeroProposta =

    # = TRATAMENTO COLUNA PropostaStatus =
    df_tratada['PropostaStatus'] = df_tratada['PropostaStatus'].str.strip()
    df_tratada['PropostaStatus'] = df_tratada['PropostaStatus'].str.upper()

    # = TRATAMENTO COLUNA BancoDigitado =
    df_tratada['BancoDigitado'] = df_tratada['BancoDigitado'].str.strip()
    df_tratada['BancoDigitado'] = df_tratada['BancoDigitado'].str.upper()

    # = TRATAMENTO COLUNA ValorContrato =
    df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.upper()
    df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace('R$', '')
    df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace('.', '')
    df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace('-', '0')
    df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace(' ', '')
    df_tratada['ValorContrato'] = df_tratada['ValorContrato'].str.replace(',', '.')
    df_tratada['ValorContrato'] = pd.to_numeric(df_tratada['ValorContrato'], downcast='float')
    df_tratada['ValorContrato'] = df_tratada['ValorContrato'].round(2)

    # = TRATAMENTO COLUNA ValorParcela =
    df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.upper()
    df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace('R$', '')
    df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace('.', '')
    df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace('-', '0')
    df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace(' ', '')
    df_tratada['ValorParcela'] = df_tratada['ValorParcela'].str.replace(',', '.')
    df_tratada['ValorParcela'] = pd.to_numeric(df_tratada['ValorParcela'], downcast='float')
    df_tratada['ValorParcela'] = df_tratada['ValorParcela'].round(2)

    # = TRATAMENTO COLUNA ValorTroco =
    df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.upper()
    df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace('R$', '')
    df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace('.', '')
    df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace('-', '0')
    df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace(' ', '')
    df_tratada['ValorTroco'] = df_tratada['ValorTroco'].str.replace(',', '.')
    df_tratada['ValorTroco'] = pd.to_numeric(df_tratada['ValorTroco'], downcast='float')
    df_tratada['ValorTroco'] = df_tratada['ValorTroco'].round(2)

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

    # = TRATAMENTO COLUNA QuantidadeParcelas =

    # = TRATAMENTO COLUNA BancoPortado =
    df_tratada['BancoPortado'] = df_tratada['BancoPortado'].str.strip()
    df_tratada['BancoPortado'] = df_tratada['BancoPortado'].str.upper()
    df_tratada['BancoPortado'] = np.where(df_tratada['BancoPortado'].isna(),
                                          'NÃO INFORMADO',
                                          df_tratada['BancoPortado'])

    # = TRATAMENTO COLUNA DataEnvioCIP =
    df_tratada['DataEnvioCIP'] = pd.to_datetime(df_tratada['DataEnvioCIP'], format='%d/%m/%Y')

    # = TRATAMENTO COLUNA DataSaldoPago =
    df_tratada['DataSaldoPago'] = np.where(df_tratada['DataSaldoPago'].isna(),
                                            'PORTABILIDADE NÃO CONFIRMADA',
                                            df_tratada['DataSaldoPago'])

    # = TRATAMENTO COLUNA OrigemCaptacao =
    df_tratada['OrigemCaptacao'] = df_tratada['OrigemCaptacao'].str.strip()
    df_tratada['OrigemCaptacao'] = df_tratada['OrigemCaptacao'].str.upper()

    # = TRATAMENTO COLUNA Orgao =
    df_tratada['Orgao'] = df_tratada['Orgao'].str.strip()
    df_tratada['Orgao'] = df_tratada['Orgao'].str.upper()

    # = TRATAMENTO COLUNA PossuiGravacao =
    df_tratada['PossuiGravacao'] = df_tratada['PossuiGravacao'].str.strip()
    df_tratada['PossuiGravacao'] = df_tratada['PossuiGravacao'].str.upper()
    df_tratada['PossuiGravacao'] = np.where(df_tratada['PossuiGravacao'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA PossuiFoto =
    df_tratada['PossuiFoto'] = df_tratada['PossuiFoto'].str.strip()
    df_tratada['PossuiFoto'] = df_tratada['PossuiFoto'].str.upper()
    df_tratada['PossuiFoto'] = np.where(df_tratada['PossuiFoto'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA EmRevisao =
    df_tratada['EmRevisao'] = df_tratada['EmRevisao'].str.strip()
    df_tratada['EmRevisao'] = df_tratada['EmRevisao'].str.upper()
    df_tratada['EmRevisao'] = np.where(df_tratada['EmRevisao'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA DataUltimoStatus =
    df_tratada['DataUltimoStatus'] = pd.to_datetime(df_tratada['DataUltimoStatus'], format='%d/%m/%Y')

    # = TRATAMENTO COLUNA PossuiPendente =
    df_tratada['PossuiPendente'] = df_tratada['PossuiPendente'].str.strip()
    df_tratada['PossuiPendente'] = df_tratada['PossuiPendente'].str.upper()
    df_tratada['PossuiPendente'] = np.where(df_tratada['PossuiPendente'] == 'SIM', True, False)

    # = TRATAMENTO COLUNA DataCriacaoProposta =
    df_tratada['DataCriacaoProposta'] = pd.to_datetime(df_tratada['DataCriacaoProposta'], format='%d/%m/%Y')

    # = Retorno da Função =
    return df_tratada
if __name__ == "__main__":
    teste = tratamento()
    print(teste)
    print(teste.info())
