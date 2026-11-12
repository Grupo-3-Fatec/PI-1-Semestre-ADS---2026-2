import telebot
import cumprimeto_de_metas as cm
import tratamento_de_dados as td
import os

#Adição de lista para armazenar os ids das mensagens a serem deletadas
id_mensagens = []

# = Botão Cumprimento de Metas =

def metas_portabilidade(botmessage):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    msg = bot.send_message(botmessage.chat.id, 'Digite a Meta Geral da Portabilidade (1.0 --- 5.0): ')
    #Armazena o id da mensagem enviada
    id_mensagens.append(msg.message_id)
    bot.register_next_step_handler(msg, metas_margem, botmessage)

def metas_margem(mensagem, botmessage):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    id_mensagens.append(mensagem.message_id)
    portabilidade = parse_float(mensagem.text)
    if portabilidade == None:
        msg = bot.send_message(botmessage.chat.id, 'Valor Inválido!')
        id_mensagens.append(msg.message_id)
        #Comando para deletar todas as mensagens armazenadas
        for id in id_mensagens:
            bot.delete_message(mensagem.chat.id, id)
        id_mensagens.clear()
        return
    msg = bot.send_message(botmessage.chat.id, 'Digite a Meta Geral da Margem (1.0 --- 5.0): ')
    id_mensagens.append(msg.message_id)
    bot.register_next_step_handler(msg, retorno, botmessage, portabilidade)

def retorno(mensagem, botmessage, portabilidade):

    import Integracao_Botoes as ib
    bot = ib.bot

    id_mensagens.append(mensagem.message_id)
    
    margem = parse_float(mensagem.text)
    if margem == None:
        msg = bot.send_message(botmessage.chat.id, 'Valor Inválido!')
        id_mensagens.append(msg.message_id)
        for id in id_mensagens:
            bot.delete_message(mensagem.chat.id, id)
        id_mensagens.clear()
        return

    
    resultado_tabela = cm.cumprimento_metas(td.tratamento(), margem, portabilidade)
    ib.salvar_dataframe_csv(resultado_tabela, 'Cumprimento_metas.csv')
    caminho_completo = os.path.join('data', 'Cumprimento_metas.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    ib.tamanho_coluna(caminho_completo)
    msg = bot.send_message(botmessage.chat.id, 'Limpando mensagens...')
    id_mensagens.append(msg.message_id)
    for id in id_mensagens:
        bot.delete_message(mensagem.chat.id, id)
    id_mensagens.clear()
    ib.enviar_arquivo(resultado_tabela, caminho_completo, botmessage)





# = Botão Comissao da Loja =

def taxa_margem(botmessage):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    msg = bot.send_message(botmessage.chat.id, 'Digite a Taxa da Margem (1.0 --- 5.0): ')
    id_mensagens.append(msg.message_id)
    bot.register_next_step_handler(msg, taxa_portabilidade, botmessage)

def taxa_portabilidade(mensagem, botmessage):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    id_mensagens.append(mensagem.message_id)
    portabilidade = parse_float(mensagem.text)
    if portabilidade == None:
        msg = bot.send_message(botmessage.chat.id, 'Valor Inválido!')
        id_mensagens.append(msg.message_id)
        for id in id_mensagens:
            bot.delete_message(mensagem.chat.id, id)
        id_mensagens.clear()
        return
    msg = bot.send_message(botmessage.chat.id, 'Digite a Taxa da Portabilidade (1.0 --- 5.0): ')
    id_mensagens.append(msg.message_id)
    bot.register_next_step_handler(msg, retorno_taxas, botmessage, portabilidade)

def retorno_taxas(mensagem, botmessage, portabilidade):

    import Integracao_Botoes as ib
    bot = ib.bot

    id_mensagens.append(mensagem.message_id)
    margem = parse_float(mensagem.text)
    if margem == None:
        msg = bot.send_message(botmessage.message.chat.id, 'Valor Inválido!')
        id_mensagens.append(msg.message_id)
        for id in id_mensagens:
            bot.delete_message(mensagem.chat.id, id)
        id_mensagens.clear()
        return

    
    tabela = ib.verifica_loja(td.tratamento(), margem, portabilidade)
    resultado_tabela = ib.comissao_loja(tabela, margem, portabilidade)
    ib.salvar_dataframe_csv(resultado_tabela, 'Comissão_Loja.csv')
    caminho_completo = os.path.join('data', 'Comissão_Loja.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    ib.tamanho_coluna(caminho_completo)
    msg = bot.send_message(botmessage.chat.id, 'Limpando mensagens...')
    id_mensagens.append(msg.message_id)
    for id in id_mensagens:
        bot.delete_message(mensagem.chat.id, id)
    id_mensagens.clear()
    ib.enviar_arquivo(resultado_tabela, caminho_completo, botmessage)





# = Botão Comissao dos Atendentes =

def chamar_atendente(botmessage):
    import Integracao_Botoes as ib

    infos = dict()
    msg = mensagem_pedido(botmessage, "taxa_margem")
    id_mensagens.append(msg.message_id)
    ib.bot.register_next_step_handler(msg, receber_mensagem, botmessage, infos, "taxa_margem")

def mensagem_pedido(botmessage, info_receber: str):
    import Integracao_Botoes as ib

    match info_receber:
        case "taxa_margem": return ib.bot.send_message(botmessage.chat.id, "Digite a Taxa da Margem (1.0 --- 5.0):")
        case "taxa_port": return ib.bot.send_message(botmessage.chat.id, "Digite a Taxa da Portabilidade (1.0 --- 5.0):")
        case "meta_margem": return ib.bot.send_message(botmessage.chat.id, "Digite a Meta Geral da Portabilidade:")
        case "meta_port": return ib.bot.send_message(botmessage.chat.id, "Digite a Meta Geral da Margem:")

def receber_mensagem(mensagem, botmessage, infos: dict, info_receber: str):
    import Integracao_Botoes as ib
    bot = ib.bot

    id_mensagens.append(mensagem.message_id)
    match info_receber:
        case "taxa_margem":
            valor = parse_float(mensagem.text)
            valor = valor / 100
            if valor == None:
                msg = ib.bot.send_message(botmessage.chat.id, "Valor Inválido!")
                id_mensagens.append(msg.message_id)
                for id in id_mensagens:
                    bot.delete_message(mensagem.chat.id, id)
                id_mensagens.clear()
                return
            valor = valor / 100
            infos[info_receber] = valor
            msg = mensagem_pedido(botmessage, "taxa_port")
            id_mensagens.append(msg.message_id)
            ib.bot.register_next_step_handler(msg, receber_mensagem, botmessage, infos, "taxa_port")
        case "taxa_port":
            valor = parse_float(mensagem.text)
            valor = valor / 100
            if valor == None:
                msg = ib.bot.send_message(botmessage.chat.id, "Valor Inválido!")
                id_mensagens.append(msg.message_id)
                for id in id_mensagens:
                    bot.delete_message(mensagem.chat.id, id)
                id_mensagens.clear()  
                return
            valor = valor / 100
            infos[info_receber] = valor
            msg = mensagem_pedido(botmessage, "meta_margem")
            id_mensagens.append(msg.message_id)
            ib.bot.register_next_step_handler(msg, receber_mensagem, botmessage, infos, "meta_margem")
        case "meta_margem":
            valor = parse_float(mensagem.text)
            if valor == None:
                msg = ib.bot.send_message(botmessage.chat.id, "Valor Inválido!")
                id_mensagens.append(msg.message_id)
                for id in id_mensagens:
                    bot.delete_message(mensagem.chat.id, id)
                id_mensagens.clear()
                return
            infos[info_receber] = valor
            msg = mensagem_pedido(botmessage, "meta_port")
            id_mensagens.append(msg.message_id)
            ib.bot.register_next_step_handler(msg, receber_mensagem, botmessage, infos, "meta_port")
        case "meta_port":
            valor = parse_float(mensagem.text)
            if valor == None:
                msg = ib.bot.send_message(botmessage.chat.id, "Valor Inválido!")
                id_mensagens.append(msg.message_id)
                for id in id_mensagens:
                    bot.delete_message(mensagem.chat.id, id)
                id_mensagens.clear()
                return
            infos[info_receber] = valor
            dados = td.tratamento()
            tabela = ib.verifica_atendentes(ib.contrato_elegivel(dados, True), infos['taxa_margem'], infos['taxa_port'])
            resultado_tabela = ib.comissao_atendente(tabela, ib.cumprimento_metas(dados, infos['meta_margem'], infos['meta_port']))
            ib.salvar_dataframe_csv(resultado_tabela, 'Comissao_Atendentes.csv')
            caminho_completo = os.path.join('data', 'Comissao_Atendentes.xlsx')
            resultado_tabela.to_excel(caminho_completo, index=False)
            ib.tamanho_coluna(caminho_completo)
            msg = bot.send_message(botmessage.chat.id, 'Limpando mensagens...')
            id_mensagens.append(msg.message_id)
            for id in id_mensagens:
                bot.delete_message(mensagem.chat.id, id)
            id_mensagens.clear()
            ib.enviar_arquivo(resultado_tabela, caminho_completo, botmessage)


def parse_float(string: str):
    try:   
        return float(string)
    except:
        return None
