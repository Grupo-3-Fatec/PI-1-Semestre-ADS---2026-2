import pandas as pd
import telebot
import os
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from Interface_Botões import bot
from FeedBack_Visual import mensagem_de_espera, apagar_mensagem_de_espera

from cumprimeto_de_metas import cumprimento_metas
from Return_Tabela import salvar_dataframe_csv
from status_documento import contrato_elegivel
from tratamento_de_dados import tratamento
from Taxa_Comissão import Comissao, receber_porcentagem
#Função importada para o comissionamento de atendentes
from comissoes import verifica_atendentes, comissao_atendente

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

def Contratos_elegiveis(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Contratos Elegíveis."
        )
    resultado = contrato_elegivel(tratamento(), True)
    salvar_dataframe_csv(resultado, 'Contratos_elegiveis.csv')
    caminho_completo = os.path.join('data', 'Contratos_elegiveis.csv')
    enviar_arquivo(resultado,caminho_completo,call)

def Contratos_nao_elegiveis(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Contratos Não Elegíveis."
    )
    resultado = contrato_elegivel(tratamento(), False)
    salvar_dataframe_csv(resultado, 'Contratos_nao_elegiveis.csv')
    caminho_completo = os.path.join('data', 'Contratos_nao_elegiveis.csv')
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
    resultado_tabela = cumprimento_metas(tabela,meta_geral_margem,meta_geral_portabilidade)
    salvar_dataframe_csv(resultado_tabela, 'Cumprimento_metas.csv')
    caminho_completo = os.path.join('data', 'Cumprimento_metas.csv')
    enviar_arquivo(resultado_tabela,caminho_completo,call)

def comissao_atendente_chamar(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Calcular Comissionamento do Atendente"
    )
    teste = verifica_atendentes(contrato_elegivel(tratamento(), True), 0.0120, 0.0140)
    resultado_tabela = comissao_atendente(teste, cumprimento_metas(tratamento(), 2000000, 1000000))
    salvar_dataframe_csv(resultado_tabela, 'Comissao_Atendentes.csv')
    caminho_completo = os.path.join('data', 'Comissao_Atendentes.csv')
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

    #As funções comentadas ainda não foram terminadas
    
    #elif call.data == "comloja":
        #comloja(call)

    elif call.data == "comatendente":
        comissao_atendente_chamar(call)

    #elif call.data == "prazos":
        #prazos(call)

    apagar_mensagem_de_espera(call, espera)
