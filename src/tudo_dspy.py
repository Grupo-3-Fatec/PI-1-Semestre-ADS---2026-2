#O que tá faltando: forma de passar os dados da planilha para o dspy como Input ou Output;
#Dar o contexto das regras de negócio para o dspy (RAG);
#Otimizar prompts;
#Integrar no Telegram.

import dspy
from typing import Literal
from config import lm_config

lm_config()

#Essa classe pega o input e analisa as signatures seguintes e decide qual delas é a mais apropriada
class SeletorContexto(dspy.Signature):
    """Analise o pedido e escolha qual classe é a mais apropriada"""
    
    pedido: str = dspy.InputField(desc="O input do usuário")

    classe_escolhida: Literal['QA', 'PlanilhaReport'] = dspy.OutputField(
        desc="Nome exato da classe a ser usada"
    )

#Essa classe ainda está wip, por enquanto é um pergunta -> resposta simples
class QA(dspy.Signature):
    """A partir da pergunta do usuário, dê uma resposta"""

    pergunta: str = dspy.InputField()
    resposta: str = dspy.OutputField(desc="resposta concisa e direta ao ponto")

#Essa classe ainda está wip, preciso de uma forma de mandar as colunas requeridas, por exemplo, para o input "faça um report de atendente x", verifica a quantidade de contratos desse atendente,
#principais tipos de proposta e bancos portados, se desses contratos quantos estão integrados ou pagos.
#Exemplo de output: "Atendente x: firmou n contratos, dos quais majoritariamente são PORTABILIDADE pelo banco INBURSA, n% dos contratos estão integrados ou pagos, tendo um bom rendimento em geral."
class PlanilhaReport(dspy.Signature):
    """A partir do pedido do usuário, entregue os dados requeridos"""

    pedido: str = dspy.InputField()
    resposta: str = dspy.OutputField(desc="O report final")

#Módulo que escolhe qual classe usar pra gerar a resposta
class Router(dspy.Module):
    def __init__(self):
        super().__init__()
        self.escolha = dspy.Predict(SeletorContexto)
        self.qa = dspy.ChainOfThought(QA)
        self.planilhareport = dspy.ChainOfThought(PlanilhaReport)

    def forward(self, pedido: str):
        escolha = self.escolha(pedido=pedido).classe_escolhida
        if escolha == "QA":
            return self.qa(pergunta=pedido)
        elif escolha == "PlanilhaReport":
            return self.planilhareport(pedido=pedido)


router = Router()
resposta = router(pedido="O que foi a crise de 1929?")

print(resposta)
