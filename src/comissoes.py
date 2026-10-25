import pandas as pd
from cumprimeto_de_metas import cumprimento_metas
from tratamento_de_dados import tratamento
from status_documento import contrato_elegivel

# = FUNÇÃO PARA VERIFICAR QUAIS CONTRATOS IRÃO RECEBER COMISSÃO =
def verifica_atendentes(contratos: pd.DataFrame, taxa_margem: float, taxa_port: float):

    # = CRIAÇÃO DO DF ANALISADO =
    analise = contratos[['Atendente','NumeroProposta','PropostaTipo','ValorContrato','ValorTroco','TaxaPorc']]

    # = FAZENDO A VERIFICACAO =
    analise_margem = analise[(analise['PropostaTipo'] == 'MARGEM') & (analise['TaxaPorc'] > taxa_margem)]
    analise_port = analise[(analise['PropostaTipo'] == 'REFIN DA PORTABILIDADE') & (analise['TaxaPorc'] > taxa_port)]

    # = JUNTANDO A DF MARGEM E PORT =
    return analise_margem.merge(analise_port, how='outer')

def comissao_atendente(contratos: pd.DataFrame, atendentes: pd.DataFrame):
    # = PLANILHA DE COMISSÃO DOS ATENDENTES =
    planilha_comissoes = atendentes

    # = COMISSÕES DA MARGEM =
    # = Filtrando Contratos MARGEM =
    analise_margem = contratos[contratos['PropostaTipo'] == 'MARGEM']

    # = Buscando Atendentes que Atingiram a Meta da Margem =
    atd_margem = atendentes.loc[atendentes['AtingiuMetaMargem'] == 'META DE MARGEM ATINGIDA', 'Atendente']
    analise_margem = analise_margem[analise_margem['Atendente'].isin(atd_margem)]

    # = Calculando a Comissão da Margem e Colocando num DF =
    analise_margem['ValorTroco'] = analise_margem['ValorTroco'] * analise_margem['TaxaPorc']
    comissao_margem = analise_margem.groupby('Atendente')['ValorTroco'].sum().reset_index()
    comissao_margem['ValorTroco'] = comissao_margem['ValorTroco'].round(2)
    comissao_margem.rename(columns={'ValorTroco': 'ComissaoMargem'}, inplace=True)
    
    # = COMISSÕES DA MARGEM =
    # = Filtrando Contratos MARGEM =
    analise_port = contratos[contratos['PropostaTipo'] == 'REFIN DA PORTABILIDADE']

    # = Buscando Atendentes que Atingiram a Meta da Margem =
    atd_port = atendentes.loc[atendentes['AtingiuMetaPortabilidade'] == 'META DE PORTABILIDADE ATINGIDA', 'Atendente']
    analise_port = analise_port[analise_port['Atendente'].isin(atd_port)]

    # = Calculando a Comissão da Margem e Colocando num DF =
    analise_port['ValorContrato'] = analise_port['ValorContrato'] * analise_port['TaxaPorc']
    comissao_port = analise_port.groupby('Atendente')['ValorContrato'].sum().reset_index()
    comissao_port['ValorContrato'] = comissao_port['ValorContrato'].round(2)
    comissao_port.rename(columns={'ValorContrato': 'ComissaoPortabilidade'}, inplace=True)

    # = Juntando os DF na Planilha =
    planilha_comissoes = planilha_comissoes.merge(comissao_port, on='Atendente', how='left')
    planilha_comissoes = planilha_comissoes.merge(comissao_margem, on='Atendente', how='left')

    # = Filtrando caso o Atendente não tenha Atingido a Meta Mostrar 0.00 =
    planilha_comissoes['ComissaoMargem'] = planilha_comissoes['ComissaoMargem'].fillna(0)
    planilha_comissoes['ComissaoPortabilidade'] = planilha_comissoes['ComissaoPortabilidade'].fillna(0)

    # = Retorno da Planilha =
    return planilha_comissoes

def verifica_loja(contratos: pd.DataFrame, taxa_margem: float, taxa_port: float) -> pd.DataFrame:

    #exclui contratos que não estão dentro da taxa pra portabilidade
    #o simbolo '~' serve apenas pra inverter a logica.
    contratos = contratos[
        ~((contratos["PropostaTipo"] == 'REFIN DA PORTABILIDADE') & 
        (contratos["TaxaPorc"] < taxa_port))        
    ]

    #repete o de cima pra margem
    contratos = contratos[
            ~((contratos["PropostaTipo"] == 'MARGEM') & 
            (contratos["TaxaPorc"] < taxa_margem))        
        ]

    return contratos

def comissao_loja(contratos: pd.DataFrame, taxa_margem_loja: float, taxa_port_loja: float) -> pd.DataFrame:
    """Retorna uma planilha com os contratos comissionaveis e seus
    valores de comissao da loja. Cada contrato aparece com seu valor de comissao"""

    #ciaçao de duas condiçoes pra contratos do tipo port e margem
    planilha_port = contratos[contratos['PropostaTipo'] == 'REFIN DA PORTABILIDADE']
    planilha_margem = contratos[contratos['PropostaTipo'] == 'MARGEM']

    #cria duas novas colunas e pra cada uma ela aplica a porcentagem de comissao no valor a ser calculado
    contratos['ComissãoPort'] = planilha_port['ValorContrato'] * taxa_port_loja
    contratos['ComissãoMargem'] = planilha_margem['ValorTroco'] * taxa_margem_loja

    return contratos[['Atendente', 'PropostaTipo', 'NumeroProposta', 'ValorContrato', 'ComissãoPort', 'ComissãoMargem']]

if __name__ == "__main__":
    teste = verifica_atendentes(contrato_elegivel(tratamento(), True), 0.0120, 0.0140)
    print(comissao_atendente(teste, cumprimento_metas(tratamento(), 2000000, 1000000)))