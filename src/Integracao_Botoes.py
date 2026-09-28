import pandas as pd
import telebot
import os
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from Interface_Botões import bot

from cumprimeto_de_metas import cumprimento_metas
from Return_Tabela import salvar_dataframe_csv
from status_documento import contrato_elegivel
from tratamento_de_dados import tratamento

def Contratos_elegiveis(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Contratos Elegíveis."
        )
    resultado = contrato_elegivel(tratamento(), True)
    salvar_dataframe_csv(resultado, 'Contratos_elegiveis.csv')
    caminho_completo = os.path.join('data', 'Contratos_elegiveis.csv')
    if not resultado.empty:
        with open(caminho_completo, 'rb') as arquivo:
            bot.send_document(
                call.message.chat.id, 
                arquivo, 
                caption=f"Pronto! Aqui está o seu arquivo:"
            )
    else:
        bot.send_message(call.message.chat.id, "O arquivo foi gerado, mas está vazio.")

def Contratos_nao_elegiveis(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Contratos Não Elegíveis."
    )
    resultado = contrato_elegivel(tratamento(), False)
    salvar_dataframe_csv(resultado, 'Contratos_nao_elegiveis.csv')
    caminho_completo = os.path.join('data', 'Contratos_nao_elegiveis.csv')
    if not resultado.empty:
        with open(caminho_completo, 'rb') as arquivo:
            bot.send_document(
                call.message.chat.id, 
                arquivo, 
                caption=f"Pronto! Aqui está o seu arquivo:"
            )
    else:
        bot.send_message(call.message.chat.id, "O arquivo foi gerado, mas está vazio.")  

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
    if not resultado_tabela.empty:
        with open(caminho_completo, 'rb') as arquivo:
            bot.send_document(
                call.message.chat.id, 
                arquivo, 
                caption=f"Pronto! Aqui está o seu arquivo:"
            )
    else:
        bot.send_message(call.message.chat.id, "O arquivo foi gerado, mas está vazio.")

def botao_clicado(call):

    # Remove o "carregando" do botão no Telegram
    bot.answer_callback_query(call.id)

    if call.data == "elegiveis":
        Contratos_elegiveis(call)

    elif call.data == "nao_elegiveis":
          Contratos_nao_elegiveis(call)

    elif call.data == "metas":
        cumprimento_metas_chamar(call)
