from Interface_Botões import bot
from cumprimeto_de_metas import cumprimento_metas
from tratamento_de_dados import tratamento


def comissao(call):
    msg = bot.send_message(
        call.message.chat.id,
        "Envie a taxa de comissão (de 1 a 5):"
    )

    bot.register_next_step_handler(msg, receber_porcentagem)


def receber_porcentagem(message):
    try:
        taxa_margem = float(message.text.replace(',', '.'))
        taxa_margem = taxa_margem / 100

    except ValueError:
            bot.send_message(
                message.chat.id,
                "Valor inválido! Digite apenas um número, como 1,20 ou 1,40."
            )
            return
    
    if taxa_margem < 0.01 or taxa_margem > 0.05:
            bot.send_message(
                message.chat.id,
                "Digite uma porcentagem entre 1 e 5."
            )
            return

    msg = bot.send_message(
        message.chat.id,
        "Agora envie a taxa de comissão da portabilidade (de 1 a 5):"
)

    bot.register_next_step_handler(msg, receber_taxa_portabilidade, taxa_margem)


#---------------------
def receber_taxa_portabilidade(message, taxa_margem):
    try:
        taxa_portabilidade = float(message.text.replace(',', '.'))
        taxa_portabilidade = taxa_portabilidade / 100

    except ValueError:
            bot.send_message(
                message.chat.id,
                "Valor inválido! Digite apenas um número, como 1,20 ou 1,40."
            )
            return
    
    if taxa_portabilidade < 0.01 or taxa_portabilidade > 0.05:
            bot.send_message(
                message.chat.id,
                "Digite uma porcentagem entre 1 e 5."
            )
            return

    df_tratada = tratamento()
            
    tabela = comissao(
        df_tratada,
        taxa_margem,
        taxa_portabilidade,
    )

    print(tabela)
#---------------------


#---------------------
def meta_portabilidade(call):

    msg = bot.send_message(
            call.message.chat.id,
            "Envie o valor da meta de portabilidade (apenas números inteiros):"
        )

    bot.register_next_step_handler(msg, receber_metaportabilidade)
#---------------------


#---------------------
def receber_metaportabilidade(message):
    try:
        valor_input_portabilidade = int(message.text)

        #---------------------
        msg = bot.send_message(
            message.chat.id,
            "Envie o valor da meta de margem (apenas números inteiros):"
        )
        bot.register_next_step_handler(msg, receber_meta_margem, valor_input_portabilidade)
        #---------------------

    except ValueError:
        bot.send_message(
            message.chat.id,
            "Valor inválido! Digite apenas números inteiros."
        )
        return
#---------------------


#---------------------
def receber_meta_margem(message, valor_input_portabilidade):
    try:
        valor_input_margem = int(message.text)

        df_tratada = tratamento()
            
        tabela = cumprimento_metas(
            df_tratada,
            valor_input_portabilidade,
            valor_input_margem,
        )

        print(tabela)

    except ValueError:
        bot.send_message(
            message.chat.id,
            "Valor inválido! Digite apenas números inteiros."
        )
        return
#---------------------

'''print(tabela)
bot.send_message(tabela)
nao sei se isso vai aqui, mas se for, é só descomentar e ver se funciona'''
