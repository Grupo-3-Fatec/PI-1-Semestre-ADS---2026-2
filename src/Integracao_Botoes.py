import pandas as pd
import telebot
import os
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
#A biblioteca abaixo só foi importada para ajustar as colunas no excel; se houver conflito, delete/comente as linhas com tamanho_coluna()
from openpyxl import load_workbook
from Interface_Botões import bot
from FeedBack_Visual import mensagem_de_espera, apagar_mensagem_de_espera

from cumprimeto_de_metas import cumprimento_metas
from Return_Tabela import salvar_dataframe_csv
from status_documento import contrato_elegivel
from tratamento_de_dados import tratamento
from Taxa_Comissão import comissao, receber_porcentagem, receber_taxa_portabilidade, meta_portabilidade, receber_metaportabilidade, receber_meta_margem
#Função importada para o comissionamento de atendentes
from comissoes import verifica_atendentes, comissao_atendente, verifica_loja, comissao_loja
from planilha_desserializada import df_dess
from Contrato_Fora_Prazo import filtrar_contratos_atrasados

#Função para enviar o arquivo e evitar repetição no código
def enviar_arquivo(tabela,caminho,call):
    if not tabela.empty:
        with open(caminho, 'rb') as arquivo:
            bot.send_document(
                call.message.chat.id, 
                arquivo, 
                caption=f"Pronto! Aqui está o seu arquivo:"
            )
    else:
        bot.send_message(call.message.chat.id, "O arquivo foi gerado, mas está vazio.")

#Função para ajustar o tamanho das colunas do excel quando enviar o arquivo; o botão ainda envia em excel sem a função, mas com as colunas não ajustadas
def tamanho_coluna(caminho):

    workbook = load_workbook(caminho)
    planilha = workbook.active

    for coluna in planilha.columns:
        maior_largura = 0
        letra_coluna = coluna[0].column_letter

        for celula in coluna:
            if celula.value is not None:
                largura = len(str(celula.value))
                if largura > maior_largura:
                    maior_largura = largura

        planilha.column_dimensions[letra_coluna].width = maior_largura + 2

    workbook.save(caminho)

def Contratos_elegiveis(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Contratos Elegíveis."
        )
    resultado = contrato_elegivel(tratamento(), True)
    #Comando para enviar o arquivo em csv antigamente
    #salvar_dataframe_csv(resultado, 'Contratos_elegiveis.csv')
    caminho_completo = os.path.join('data', 'Contratos_elegiveis.xlsx')
    resultado.to_excel(caminho_completo, index=False)
    tamanho_coluna(caminho_completo)
    enviar_arquivo(resultado,caminho_completo,call)

def Contratos_nao_elegiveis(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Contratos Não Elegíveis."
    )
    resultado = contrato_elegivel(tratamento(), False)
    #salvar_dataframe_csv(resultado, 'Contratos_nao_elegiveis.csv')
    caminho_completo = os.path.join('data', 'Contratos_nao_elegiveis.xlsx')
    resultado.to_excel(caminho_completo, index=False)
    tamanho_coluna(caminho_completo)
    enviar_arquivo(resultado,caminho_completo,call)  

def cumprimento_metas_chamar(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Cumprimento de Metas."
    )
    tabela = tratamento()
    #esses dados estão como teste:
    meta_geral_margem = 1000000
    meta_geral_portabilidade = 2000000
    porcentagem = 0.01
    resultado_tabela = cumprimento_metas(tabela,meta_geral_margem,meta_geral_portabilidade,porcentagem)
    #salvar_dataframe_csv(resultado_tabela, 'Cumprimento_metas.csv')
    caminho_completo = os.path.join('data', 'Cumprimento_metas.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    tamanho_coluna(caminho_completo)
    enviar_arquivo(resultado_tabela,caminho_completo,call)

def comissao_loja_chamar(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Calcular Comissionamento da Loja"
    )
    #esses dados estão apenas como teste
    teste = verifica_loja(contrato_elegivel(tratamento(), True), 0.0120, 0.0140)
    resultado_tabela = comissao_loja(teste, 0.120, 0.0140)
    #salvar_dataframe_csv(resultado_tabela, 'Comissao_Loja.csv')
    caminho_completo = os.path.join('data', 'Comissao_Loja.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    tamanho_coluna(caminho_completo)
    enviar_arquivo(resultado_tabela,caminho_completo,call)

def comissao_atendente_chamar(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Calcular Comissionamento do Atendente"
    )
    teste = verifica_atendentes(contrato_elegivel(tratamento(), True), 0.0120, 0.0140)
    resultado_tabela = comissao_atendente(teste, cumprimento_metas(tratamento(), 2000000, 1000000, 0.01))
    #salvar_dataframe_csv(resultado_tabela, 'Comissao_Atendentes.csv')
    caminho_completo = os.path.join('data', 'Comissao_Atendentes.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    tamanho_coluna(caminho_completo)
    enviar_arquivo(resultado_tabela,caminho_completo,call)

def alerta_prazos(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Alerta de Prazos"
    )
    tabela = tratamento()
    resultado_tabela = filtrar_contratos_atrasados(tabela, 15)
    bot.send_message(
        call.message.chat.id,
        f"Relatório gerado com sucesso! {len(resultado_tabela)} contratos encontrados com mais de 15 dias."
    )
    #salvar_dataframe_csv(resultado_tabela, 'Alerta_Prazos.csv')
    caminho_completo = os.path.join('data', 'Alerta_Prazos.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    tamanho_coluna(caminho_completo)
    enviar_arquivo(resultado_tabela,caminho_completo,call)

def botao_clicado(call):

    # Remove o "carregando" do botão no Telegram
    bot.answer_callback_query(call.id)

    espera = mensagem_de_espera(call)

    if call.data == "elegiveis":
        Contratos_elegiveis(call)

    elif call.data == "nao_elegiveis":
          Contratos_nao_elegiveis(call)

    elif call.data == "metas":
        Comissao(call)
        cumprimento_metas_chamar(call)

    elif call.data == "comloja":
        comissao_loja_chamar(call)

    elif call.data == "comatendente":
        comissao_atendente_chamar(call)

    elif call.data == "prazos":
        alerta_prazos(call)

    apagar_mensagem_de_espera(call, espera)
