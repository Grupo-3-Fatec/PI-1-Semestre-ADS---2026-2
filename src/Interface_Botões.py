import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

# =========================
# CONFIG
# =========================

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


from Integracao_Botoes import botao_clicado


# =========================
# FUNÇÃO: CRIAR BOTÕES
# =========================

def criar_botoes():
    botoes = InlineKeyboardMarkup()

    botoes.add(
        InlineKeyboardButton(
            "Contratos Elegíveis",
            callback_data="elegiveis"
        )
    )
    botoes.add(
            InlineKeyboardButton(
                "Contratos Não Elegíveis",
                callback_data="nao_elegiveis"
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
    )

#aqui

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