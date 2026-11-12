import telebot
import os
import tempfile
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# =========================
# CONFIG
# =========================

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


from Integracao_Botoes import botao_clicado

#Adicionado pela feat(REB-22)
from seletor_de_funcao import processar_mensagem, processar_mensagem_audio

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
    botoes.add(
        InlineKeyboardButton(
            "Calcular Comissionamento da Loja",
            callback_data="comloja"
        )
    )
    botoes.add(
        InlineKeyboardButton(
            "Calcular Comissionamento do Atendente",
            callback_data="comatendente"
        )
    )
    botoes.add(
        InlineKeyboardButton(
            "Alerta de Prazos",
            callback_data="prazos"
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

#Adicionado pela feat(REB-22) para receber mensagens de texto
@bot.message_handler(content_types=['text'])
def responder_texto(message):
    try:
        resultado = processar_mensagem(message.text, message)
    except Exception as e:
        print(f"[ERRO processar_mensagem] {e}")
        bot.send_message(message.chat.id, "Ocorreu um erro ao processar sua mensagem.")
        return

    # Se o seletor devolveu string (caso QA ou fallback), envia no Telegram
    if isinstance(resultado, str) and resultado.strip():
        bot.send_message(message.chat.id, resultado)


@bot.message_handler(content_types=['audio','voice'])
def responder_audio(message):
    try:

        if message.content_type == 'audio':
            bot.send_message(message.chat.id, 'Arquivos de áudios não são permitidos. Utilize o gravador do chat.')
            return

        file_id = message.voice.file_id

        file_path = bot.get_file(file_id).file_path

        file = bot.download_file(file_path)

        with tempfile.NamedTemporaryFile(suffix='.ogg', delete=False) as arquivo:
            arquivo.write(file)
            file_path = arquivo.name

        return processar_mensagem_audio(file_path)
        
    except Exception as e:
        print(f'[ERRO processar_mensagem_audio] {e}')
        bot.send_message(message.chat.id, 'Ocorreu um erro ao processar o audio')
        return


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
