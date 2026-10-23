# O que tá faltando: Botar docstring em todas as funções pro dspy poder passar o contexto pra llm;
# Colocar as outras funções
# Integrar no Telegram.

import dspy
from config import lm_config
from Integracao_Botoes import (
    Contratos_elegiveis,
    Contratos_nao_elegiveis,
    cumprimento_metas_chamar,
    comissao_loja_chamar,
    comissao_atendente_chamar,
    alerta_prazos,
)


lm_config()

# Essa classe pega o input e decide qual das funções é a mais apropriada.
class SeletorContexto(dspy.Signature):
    """Analise o input do usuário e decide qual função chamar."""
    # Input do usuário
    user_input: str = dspy.InputField(desc="O pedido ou pergunta digitada pelo usuário.")
    # Vai retornar o nome de uma dessas funções e classe
    funcao_ou_classe_escolhida: str = dspy.OutputField(
        desc="Nome da função ou classe a ser usada: 'comissao_loja_chamar', 'cumprimento_metas_chamar', 'contratos_elegiveis'," \
        "'comissao_atendente_chamar', 'alerta_prazos', 'contratos_nao_elegiveis', 'QA'."
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
    """
    Decide o que fazer com a mensagem de texto.

    Retornos:
      - str  → resposta do QA (o handler do Telegram deve enviar).
      - None → as funções de arquivo já enviaram o que tinham que enviar.
    """
    decisao = dspy.Predict(SeletorContexto)(user_input=mensagem)
    escolha = decisao.funcao_ou_classe_escolhida.lower()

    # QA — retorna string; quem chama envia no Telegram
    if "qa" in escolha:
        return dspy.Predict(QA)(user_input=mensagem).resposta

    # Pega a string da variável funcao_ou_classe_escolhida e vê se tem o nome certo dentro
    if "contratos_nao_elegiveis" in escolha:
        Contratos_nao_elegiveis(call)
    elif "contratos_elegiveis" in escolha:
        Contratos_elegiveis(call)
    elif "cumprimento_metas_chamar" in escolha:
        cumprimento_metas_chamar(call)
    elif "comissao_loja_chamar" in escolha:
        comissao_loja_chamar(call)
    elif "comissao_atendente_chamar" in escolha:
        comissao_atendente_chamar(call)
    elif "alerta_prazos" in escolha:
        alerta_prazos(call)
    else:
        return "Não entendi sua mensagem."

    return None

# Isso é só teste
if __name__=="__main__":
    print(processar_mensagem("Quem matou Osama Bin Laden?", chat_id=0))
    print(processar_mensagem("quero ver os contratos não elegiveis", chat_id=0))
# Essa linha verifica o raciocínio racional
dspy.inspect_history(n=1)
