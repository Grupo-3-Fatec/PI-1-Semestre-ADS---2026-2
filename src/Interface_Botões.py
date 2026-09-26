import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


# =========================
# CONFIG
# =========================

TOKEN = "8996796895:AAE4b3B2LHOoQkgCBamW6QYpdmMWWAsnE6s"

bot = telebot.TeleBot(TOKEN)


from Integracao_Botoes import botao_clicado


# =========================
# FUNÇÃO: CRIAR BOTÕES
# =========================

def criar_botoes():
    botoes = InlineKeyboardMarkup()

    botoes.add(
        InlineKeyboardButton(
            "Criar Planilha",
            callback_data="criar_planilha"
        )
    )

    botoes.add(
        InlineKeyboardButton(
            "Filtrar Dados da Planilha",
            callback_data="dados_planilha"
        )
    )

    botoes.add(
        InlineKeyboardButton(
            "Retornar requisições da Planilha",
            callback_data="requisicoes_planilha"
        )
    )

    botoes.add(
        InlineKeyboardButton(
            "Eliminar Riscos de Compliance",
            callback_data="risco_compliance"
        )
    )

    botoes.add(
        InlineKeyboardButton(
            "Cumprimento de Metas",
            callback_data="metas"
        )
    )

    return botoes


# =========================
# FUNÇÃO: MENSAGEM INICIAL
# =========================

# Mensagem inicial que o bot vai enviar
# junto com os botões

def mensagem_inicial():
    return (
        "Olá! Seja bem-vindo ao nosso atendimento.\n"
        "Para começar, selecione uma das opções abaixo:\n\n"

        "CRIAR PLANILHA\n\n"

        "FILTRAR DADOS\n"
        "Filtre os dados desejados.\n\n"

        "RETORNAR REQUISIÇÕES DA PLANILHA\n"
        "Buscar na planilha as requisições que foram registradas e mostrar.\n\n"

        "ELIMINAR RISCOS DE COMPLIANCE\n"
        "Evitar situações que façam a empresa descumprir regras.\n\n"

        "CUMPRIMENTO DE METAS\n"
    )

#aqui

# # =========================
# # FUNÇÃO: CRIAR PLANILHA
# # =========================

# def criar_planilha(call):
#     bot.send_message(
#         call.message.chat.id,
#         "Você selecionou: Criar Planilha."
#     )


# # =========================
# # FUNÇÃO: FILTRAR DADOS
# # =========================

# def filtrar_dados(call):
#     bot.send_message(
#         call.message.chat.id,
#         "Você selecionou: Filtrar Dados da Planilha."
#     )


# # =========================
# # FUNÇÃO: REQUISIÇÕES
# # =========================

# def retornar_requisicoes(call):
#     bot.send_message(
#         call.message.chat.id,
#         "Você selecionou: Retornar requisições da Planilha."
#     )


# # =========================
# # FUNÇÃO: COMPLIANCE
# # =========================

# def eliminar_riscos_compliance(call):
#     bot.send_message(
#         call.message.chat.id,
#         "Você selecionou: Eliminar Riscos de Compliance."
#     )


# # =========================
# # FUNÇÃO: METAS
# # =========================

# def cumprimento_metas(call):
#     bot.send_message(
#         call.message.chat.id,
#         "Você selecionou: Cumprimento de Metas."
#     )




# =========================
# FUNÇÃO: /START
# =========================

# Assim que o usuário der o comando /start
# o Telegram envia uma mensagem junto com os botões clicáveis
#comando start pode ser alterado por outra palavra


@bot.message_handler(commands=["start"])
def start(message):
    botoes = criar_botoes()
    texto = mensagem_inicial()

    bot.send_message(
        message.chat.id,
        texto,
        reply_markup=botoes
    )


# =========================
# BOTÕES
# =========================

# Aqui o código identifica qual botão foi pressionado

@bot.callback_query_handler(func=lambda call: True)
def botao(call):

    botao_clicado(call)

    # Remove o "carregando" do botão no Telegram
    # bot.answer_callback_query(call.id)

    # if call.data == "criar_planilha":
    #     criar_planilha(call)

    # elif call.data == "dados_planilha":
    #     filtrar_dados(call)

    # elif call.data == "requisicoes_planilha":
    #     retornar_requisicoes(call)

    # elif call.data == "risco_compliance":
    #     eliminar_riscos_compliance(call)

    # elif call.data == "metas":
    #     cumprimento_metas_chamar(call)


# =========================
# INICIAR BOT
# =========================

def iniciar_bot():
    print("Bot iniciado...")
    bot.infinity_polling()


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    iniciar_bot()