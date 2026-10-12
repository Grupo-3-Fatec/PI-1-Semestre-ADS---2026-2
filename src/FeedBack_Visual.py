from Interface_Botões import bot


def mensagem_de_espera(call):
    mensagem = bot.send_message(
        call.message.chat.id,
        text="Sua resposta esta sendo gerada, aguarde um momento..."
    )
    return mensagem

def apagar_mensagem_de_espera(call, mensagem):
    bot.delete_message(
        mensagem.chat.id,
        mensagem.message_id
    )

