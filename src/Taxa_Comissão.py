import telebot
import cumprimeto_de_metas as cm
import tratamento_de_dados as td
import os

# = Botão Cumprimento de Metas =

def metas_portabilidade(call):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    msg = bot.send_message(call.message.chat.id, 'Digite a Meta Geral da Portabilidade (1.0 --- 5.0): ')
    bot.register_next_step_handler(msg, metas_margem, call)

def metas_margem(mensagem, call):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    portabilidade = parse_float(mensagem.text)
    if portabilidade == None:
        bot.send_message(call.message.chat.id, 'Valor Inválido!')
        return
    msg = bot.send_message(call.message.chat.id, 'Digite a Meta Geral da Margem (1.0 --- 5.0): ')
    bot.register_next_step_handler(msg, retorno, call, portabilidade)

def retorno(mensagem, call, portabilidade):

    margem = parse_float(mensagem.text)
    if margem == None:
        bot.send_message(call.message.chat.id, 'Valor Inválido!')
        return

    import Integracao_Botoes as ib
    bot = ib.bot
    
    resultado_tabela = cm.cumprimento_metas(td.tratamento(), margem, portabilidade)
    ib.salvar_dataframe_csv(resultado_tabela, 'Cumprimento_metas.csv')
    caminho_completo = os.path.join('data', 'Cumprimento_metas.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    ib.tamanho_coluna(caminho_completo)
    ib.enviar_arquivo(resultado_tabela, caminho_completo, call)





# = Botão Comissao da Loja =

def taxa_margem(call):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    msg = bot.send_message(call.message.chat.id, 'Digite a Taxa da Margem (1.0 --- 5.0): ')
    bot.register_next_step_handler(msg, taxa_portabilidade, call)

def taxa_portabilidade(mensagem, call):
    
    import Integracao_Botoes as ib
    bot = ib.bot

    portabilidade = parse_float(mensagem.text)
    if portabilidade == None:
        bot.send_message(call.message.chat.id, 'Valor Inválido!')
        return
    msg = bot.send_message(call.message.chat.id, 'Digite a Taxa da Portabilidade (1.0 --- 5.0): ')
    bot.register_next_step_handler(msg, retorno_taxas, call, portabilidade)

def retorno_taxas(mensagem, call, portabilidade):

    margem = parse_float(mensagem.text)
    if margem == None:
        bot.send_message(call.message.chat.id, 'Valor Inválido!')
        return

    import Integracao_Botoes as ib
    bot = ib.bot
    
    tabela = ib.verifica_loja(td.tratamento(), margem, portabilidade)
    resultado_tabela = ib.comissao_loja(tabela, margem, portabilidade)
    ib.salvar_dataframe_csv(resultado_tabela, 'Comissão_Loja.csv')
    caminho_completo = os.path.join('data', 'Comissão_Loja.xlsx')
    resultado_tabela.to_excel(caminho_completo, index=False)
    ib.tamanho_coluna(caminho_completo)
    ib.enviar_arquivo(resultado_tabela, caminho_completo, call)





# = Botão Comissao dos Atendentes =

def chamar_atendente(call):
    import Integracao_Botoes as ib

    infos = dict()
    msg = mensagem_pedido(call, "taxa_margem")
    ib.bot.register_next_step_handler(msg, receber_mensagem, call, infos, "taxa_margem")

def mensagem_pedido(call, info_receber: str):
    import Integracao_Botoes as ib

    match info_receber:
        case "taxa_margem": return ib.bot.send_message(call.message.chat.id, "Digite a Taxa da Margem (1.0 --- 5.0):")
        case "taxa_port": return ib.bot.send_message(call.message.chat.id, "Digite a Taxa da Portabilidade (1.0 --- 5.0):")
        case "meta_margem": return ib.bot.send_message(call.message.chat.id, "Digite a Meta Geral da Portabilidade:")
        case "meta_port": return ib.bot.send_message(call.message.chat.id, "Digite a Meta Geral da Margem:")

def receber_mensagem(mensagem, call, infos: dict, info_receber: str):
    import Integracao_Botoes as ib
    
    match info_receber:
        case "taxa_margem":
            valor = parse_float(mensagem.text)
            valor = valor / 100
            if valor == None:
                ib.bot.send_message(call.message.chat.id, "Valor Inválido!")
                return
            infos[info_receber] = valor
            msg = mensagem_pedido(call, "taxa_port")
            ib.bot.register_next_step_handler(msg, receber_mensagem, call, infos, "taxa_port")
        case "taxa_port":
            valor = parse_float(mensagem.text)
            valor = valor / 100
            if valor == None:
                ib.bot.send_message(call.message.chat.id, "Valor Inválido!")
                return
            infos[info_receber] = valor
            msg = mensagem_pedido(call, "meta_margem")
            ib.bot.register_next_step_handler(msg, receber_mensagem, call, infos, "meta_margem")
        case "meta_margem":
            valor = parse_float(mensagem.text)
            if valor == None:
                ib.bot.send_message(call.message.chat.id, "Valor Inválido!")
                return
            infos[info_receber] = valor
            msg = mensagem_pedido(call, "meta_port")
            ib.bot.register_next_step_handler(msg, receber_mensagem, call, infos, "meta_port")
        case "meta_port":
            valor = parse_float(mensagem.text)
            if valor == None:
                ib.bot.send_message(call.message.chat.id, "Valor Inválido!")
                return
            infos[info_receber] = valor
            dados = td.tratamento()
            tabela = ib.verifica_atendentes(ib.contrato_elegivel(dados, True), infos['taxa_margem'], infos['taxa_port'])
            resultado_tabela = ib.comissao_atendente(tabela, ib.cumprimento_metas(dados, infos['meta_margem'], infos['meta_port']))
            ib.salvar_dataframe_csv(resultado_tabela, 'Comissao_Atendentes.csv')
            caminho_completo = os.path.join('data', 'Comissao_Atendentes.xlsx')
            resultado_tabela.to_excel(caminho_completo, index=False)
            ib.tamanho_coluna(caminho_completo)
            ib.enviar_arquivo(resultado_tabela, caminho_completo, call)


def parse_float(string: str):
    try:   
        return float(string)
    except:
        return None