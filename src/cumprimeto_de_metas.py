import pandas as pd
import numpy as np
from tratamento_de_dados import tratamento

def cumprimento_metas(df_tratada, meta_geral_margem, meta_geral_portabilidade):
    # = Delimitando Tabela de Análise =
    analise = df_tratada[['Atendente','Cliente','ValorContrato','ValorTroco','PropostaTipo']]

    # = Delimitando Tabela de Retorno
    planilha_metas = pd.DataFrame(columns=['Atendente','ValorVendasPortabilidade','ValorVendasMargem','AtingiuMetaPortabilidade','AtingiuMetaMargem'])

    # = Associando Atendentes =
    planilha_metas['Atendente'] = analise['Atendente'].unique()
    numero_atendentes = analise['Atendente'].count()

    # = Delimitando Meta da Portabilidade =
    meta_portabilidade = meta_geral_portabilidade / numero_atendentes

    # = Delimitando Meta da Margem =
    meta_margem = meta_geral_margem / numero_atendentes

    # = Calculando Vendas de cada Tipo =
    vendas_portabilidade = analise[analise['PropostaTipo'] == 'REFIN DA PORTABILIDADE'].groupby('Atendente')['ValorContrato'].sum().values
    vendas_margem = analise[analise['PropostaTipo'] == 'MARGEM'].groupby('Atendente')['ValorTroco'].sum().values

    # = Preenchendo Tabela de Retorno =
    planilha_metas['ValorVendasPortabilidade'] = vendas_portabilidade
    planilha_metas['ValorVendasMargem'] = vendas_margem
    planilha_metas['AtingiuMetaPortabilidade'] = np.where(planilha_metas['ValorVendasPortabilidade'] > meta_portabilidade,
                                                          'META DE PORTABILIDADE ATINGIDA',
                                                          'META DE PORTABILIDADE NÃO ATINGIDA')
    planilha_metas['AtingiuMetaMargem'] = np.where(planilha_metas['ValorVendasMargem'] > meta_margem,
                                                   'META DE MARGEM ATINGIDA',
                                                   'META DE MARGEM NÃO ATINGIDA')

    # = Retornando Tabela =
    return planilha_metas
if __name__ == "__main__":
    teste = cumprimento_metas(tratamento(), 2000000, 1000000)
    print(teste)