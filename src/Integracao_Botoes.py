import pandas as pd
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
# =========================
# FUNÇÃO: CRIAR PLANILHA
# =========================

from Interface_Botões import bot

from cumprimeto_de_metas import cumprimento_metas
from data_filter import singleDataFilter
from Return_Tabela import salvar_dataframe_csv
from status_documento import contrato_elegivel, sem_documento, sem_gravacao
from tratamento_de_dados import tratamento

def criar_planilha(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Criar Planilha."
    )
    tabela = tratamento()
    #usa a função tratamento() para transformar o data.csv no df_tratada exigida pelo salvar_dataframe_csv
    if tabela is None or tabela.empty:
            bot.send_message(call.message.chat.id, "Aviso: DataFrame vazio.")
    #Se o dataframe estiver vazio, envia uma mensagem de erro,
    #como foi pedido para adicionar na função original
    nome_arquivo = 'data_tratada.csv'
    salvar_dataframe_csv(tabela,nome_arquivo)
    bot.send_message(call.message.chat.id, "Arquivo criado com sucesso. Olhe seu diretório.")

# =========================
# FUNÇÃO: FILTRAR DADOS
# =========================

def filtrar_dados(call):
        #O programa vai mostrar mais 3 botões ao selecionar 'Filtrar Dados', correspondente as 3 funções de retorno de dados:
    botoesfiltro = [
            [
                InlineKeyboardButton(
                    "VER CONTRATOS QUE NÃO POSSUEM GRAVAÇÃO",
                    callback_data="sem_gravacao"
                )
            ],
            [
                InlineKeyboardButton(
                    "VER CONTRATOS QUE NÃO POSSUEM FOTO/GRAVAÇÃO",
                    callback_data="sem_documento"
                )
            ],
            [
                InlineKeyboardButton(
                    "VER CONTRATOS QUE POSSUEM FOTO/GRAVAÇÃO",
                    callback_data="contrato_elegivel"
                )
            ]
        ]

    tecladofiltro = InlineKeyboardMarkup(botoesfiltro)
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Filtrar Dados da Planilha. Selecione uma das opções abaixo:",
        reply_markup = tecladofiltro
    )

def sem_gravacao_chamar(call):
        resultado = sem_gravacao(tratamento())
        #executa a função sem_gravacao e envia pela mensagem do telegram pelo comando abaixo:
        TAMANHO_MAXIMO = 4000
        #como o limite de characteres por mensagem do telegram é ~4000, 
        #se a mensagem for maior, o comando irá separar o conteúdo em mensagens diferentes
        if len(resultado) > TAMANHO_MAXIMO:
            posicao = 0

            while posicao < len(resultado):
                mensagem = resultado[posicao:posicao + TAMANHO_MAXIMO]

                bot.send_message(
                    call.message.chat.id,
                    mensagem
                )

                posicao += TAMANHO_MAXIMO
        else:
            bot.send_message(
                call.message.chat.id,
                resultado
            )

def sem_documento_chamar(call):
        resultado = sem_documento(tratamento())
        TAMANHO_MAXIMO = 4000

        if len(resultado) > TAMANHO_MAXIMO:
            posicao = 0

            while posicao < len(resultado):
                mensagem = resultado[posicao:posicao + TAMANHO_MAXIMO]

                bot.send_message(
                    call.message.chat.id,
                    mensagem
                )

                posicao += TAMANHO_MAXIMO
        else:
            bot.send_message(
                call.message.chat.id,
                resultado
            )

def contrato_elegivel_chamar(call):
        resultado = contrato_elegivel(tratamento())
        TAMANHO_MAXIMO = 4000

        if len(resultado) > TAMANHO_MAXIMO:
            posicao = 0

            while posicao < len(resultado):
                mensagem = resultado[posicao:posicao + TAMANHO_MAXIMO]

                bot.send_message(
                    call.message.chat.id,
                    mensagem
                )

                posicao += TAMANHO_MAXIMO
        else:
            bot.send_message(
                call.message.chat.id,
                resultado
            )

# =========================
# FUNÇÃO: REQUISIÇÕES
# =========================

def retornar_requisicoes(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Retornar requisições da Planilha."
    )
    #Adicionar os valores correspondentes
    coluna = "<adicionar_coluna>"
    valor = "<adicionar_valor>"
    bot.send_message(
            call.message.chat.id,
            f"As requisições atuais são:\nColuna:{coluna}\ne\nValor:{valor}"
        )
    resultado = singleDataFilter(coluna, valor)
    TAMANHO_MAXIMO = 4000

    if len(resultado) > TAMANHO_MAXIMO:
            posicao = 0

            while posicao < len(resultado):
                mensagem = resultado[posicao:posicao + TAMANHO_MAXIMO]

                bot.send_message(
                    call.message.chat.id,
                    mensagem
                )

                posicao += TAMANHO_MAXIMO
    else:
            bot.send_message(
                call.message.chat.id,
                resultado
            )


# =========================
# FUNÇÃO: COMPLIANCE
# =========================

def eliminar_riscos_compliance(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Eliminar Riscos de Compliance."
    )
    #Não consegui achar se alguém fez a função para esse botão, ou se ainda está em produção/análise


# =========================
# FUNÇÃO: METAS
# =========================

def cumprimento_metas_chamar(call):
    bot.send_message(
        call.message.chat.id,
        "Você selecionou: Cumprimento de Metas."
    )
    tabela = tratamento()
    #esses dados estão como teste:
    meta_geral_margem = "<adicionar_valor>"
    meta_geral_portabilidade = "<adicionar_valor>"
    resultado_tabela = cumprimento_metas(tabela,meta_geral_margem,meta_geral_portabilidade)
    resultado = resultado_tabela.to_string(index=False)
    TAMANHO_MAXIMO = 4000

    if len(resultado) > TAMANHO_MAXIMO:
            posicao = 0

            while posicao < len(resultado):
                mensagem = resultado[posicao:posicao + TAMANHO_MAXIMO]

                bot.send_message(
                    call.message.chat.id,
                    mensagem
                )

                posicao += TAMANHO_MAXIMO
    else:
            bot.send_message(
                call.message.chat.id,
                resultado
            )



def botao_clicado(call):

    # Remove o "carregando" do botão no Telegram
    bot.answer_callback_query(call.id)

    if call.data == "criar_planilha":
        criar_planilha(call)

    elif call.data == "dados_planilha":
        filtrar_dados(call)

    elif call.data == "sem_gravacao":
        sem_gravacao_chamar(call)

    elif call.data == "sem_documento":
        sem_documento_chamar(call)

    elif call.data == "contrato_elegivel":
        contrato_elegivel_chamar(call)

    elif call.data == "requisicoes_planilha":
        retornar_requisicoes(call)

    elif call.data == "risco_compliance":
        eliminar_riscos_compliance(call)

    elif call.data == "metas":
        cumprimento_metas_chamar(call)
