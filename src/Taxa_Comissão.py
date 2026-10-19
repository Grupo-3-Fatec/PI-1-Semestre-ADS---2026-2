from Interface_Botões import bot

def Comissao(call):
    msg = bot.send_message(
        call.message.chat.id,
        "Envie o valor do cumprimento de metas em porcentagem:"
    )

    bot.register_next_step_handler(msg, receber_porcentagem)

def receber_porcentagem(message):
    print(message.text)