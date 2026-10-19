from Interface_Botões import bot


def mensagem_de_espera(call):
    mensagem = bot.send_message(
        call.message.chat.id,
        text="Sua resposta esta sendo gerada, aguarde um momento..."
)
    return mensagem

bot delete_message(
        mensagem.chat.id,
        mensagem.message_id
)




#por enquanto é so isso que da pra fazer com os codigos que ja temos
#tem que esperar os novos botoes e as parte de mensagem que a gente envia


#basicamente é so fazer o aruivo que tem os botoes chamar essa função
  

