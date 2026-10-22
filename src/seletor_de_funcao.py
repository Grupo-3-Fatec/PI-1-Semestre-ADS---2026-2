# O que tá faltando: Botar docstring em todas as funções pro dspy poder passar o contexto pra llm;
# Colocar as outras funções
# Integrar no Telegram.

import os
import dspy
import telebot
from config import lm_config
from Interface_Botões import bot
from Integracao_Botoes import Contratos_elegiveis, Contratos_nao_elegiveis, cumprimento_metas_chamar

lm_config()

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Essa classe pega o input e decide qual das funções é a mais apropriada.
class SeletorContexto(dspy.Signature):
    """Analise o input do usuário e decide qual função chamar."""
    # Input do usuário
    user_input: str = dspy.InputField(desc="O pedido ou pergunta digitada pelo usuário.")
    # Vai retornar o nome de uma dessas funções e classe
    funcao_ou_classe_escolhida: str = dspy.OutputField(
        desc="Nome da função ou classe a ser usada: 'cumprimento_de_metas', 'contratos_elegiveis', 'contratos_nao_elegiveis', 'QA'."
    )

# Essa classe por enquanto é um pergunta -> resposta simples
class QA(dspy.Signature):
    """
    **SOMENTE USE ESSA CLASSE SE O INPUT NÃO SE ENQUADRAR EM NENHUMA DAS FUNÇÕES**
    A partir do input do usuário, dê uma resposta."""

    user_input: str = dspy.InputField()
    resposta: str = dspy.OutputField(desc="resposta concisa e direta ao ponto")

# Essa função chama as funções (kkkk)
def processar_mensagem(mensagem: str, call):

    # Pega o input e outputa o nome de uma das funções
    decisao = dspy.Predict(SeletorContexto)(user_input=mensagem)
    # Pega a string da variável funcao_ou_classe_escolhida e vê se tem o nome certo dentro
    if "QA" in decisao.funcao_ou_classe_escolhida:
        return dspy.Predict(QA)(user_input=mensagem).resposta

    elif "cumprimento_de_metas" in decisao.funcao_ou_classe_escolhida:
        return cumprimento_metas_chamar(call)

    elif "contratos_elegiveis" in decisao.funcao_ou_classe_escolhida:
        return Contratos_elegiveis(call)

    elif "contratos_nao_elegiveis" in decisao.funcao_ou_classe_escolhida:
        return Contratos_nao_elegiveis(call)

    else:
        return bot.send_message(call.message.chat.id, "Não entendi sua mensagem.")

# Isso é só teste
"""if __name__=="__main__":
    print(processar_mensagem("Quem matou Osama Bin Laden?"))
    print(processar_mensagem("quero ver os contratos não elegiveis"))
# Essa linha verifica o raciocínio racional
dspy.inspect_history(n=1)"""
