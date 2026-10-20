from Interface_Botões import bot
from cumprimeto_de_metas import cumprimento_metas 

def Comissao(call):
    msg = bot.send_message(
        call.message.chat.id,
        "Envie o valor do cumprimento de metas em porcentagem(apenas numeros, como 0.02 ou 0.12):"
    )

    bot.register_next_step_handler(msg, receber_porcentagem)

def receber_porcentagem(message):
    try:
        porcentagem = float(message.text.replace(',', '.'))

    except ValueError:
            bot.send_message(
                message.chat.id,
                "Valor inválido! Digite apenas um número, como 0.02 ou 0.12."
            )
            return
    
    if porcentagem < 0 or porcentagem > 5:
            bot.send_message(
                message.chat.id,
                "Digite uma porcentagem entre 0.01 e 5."
            )
            return

    df_tratada = tratamento()

tabela = cumprimento_metas(
    df_tratada,
    2000000,
    1000000,
    porcentagem
)

print(tabela)
'''bot.send_message(tabela)
nao sei se isso vai aqui, mas se for, é só descomentar e ver se funciona'''
