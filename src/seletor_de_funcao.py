import re
import dspy
from pypdf import PdfReader
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

# Essa função extrai e fragmenta o texto do PDF
def carregar_textos_pdf(caminho_pdf: str) -> list[str]:
    leitor = PdfReader(caminho_pdf)
    texto_total = ""

    # Extrai o texto inteiro
    for pagina in leitor.pages:
        texto_pagina = pagina.extract_text()
        if texto_pagina:
            texto_total += texto_pagina + "\n"

    # Quebra o texto bruto em pedaços menores, utilizando Regex para separar por artigos para melhorar o RAG, 
    # veja mais em: https://www.mongodb.com/resources/basics/chunking-explained
    padrao_artigos = r"(?=Art\.\s*\d+[ºª]?)"
    artigos_brutos = re.split(padrao_artigos, texto_total)
    chunks_por_artigo = [artigo.strip() for artigo in artigos_brutos if len(artigo.strip()) > 30]

    return chunks_por_artigo


# Essa classe pega o input e decide qual das funções é a mais apropriada
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
    Responda à pergunta do usuário. 
    Use as passagens do contexto fornecido se elas forem relevantes. 
    Caso a informação não esteja no contexto, utilize seu próprio conhecimento geral para responder de forma precisa.
    """

    contexto: str = dspy.InputField(desc="Passagens relevantes recuperadas da base de conhecimento")
    user_input: str = dspy.InputField()
    resposta: str = dspy.OutputField(desc="Resposta direta, factual e atualizada.")

# Essa classe organiza o texto a ser passado para contextualizar o prompt
class RAG(dspy.Module):
    def __init__(self, passagens: list[str], num_passages=3):
        super().__init__()
        self.passagens = passagens
        self.num_passages = num_passages
        self.gerar_resposta = dspy.ChainOfThought(QA)

    def forward(self, user_input):
        # Busca no input palavras com mais de 3 letras
        palavras_chave = [p.lower() for p in user_input.split() if len(p) > 3]

        # Pontua os blocos do PDF com base em quantas ocorrências das palavras foram encontradas
        blocos_pontuados = []
        for bloco in self.passagens:
            score = sum(1 for palavra in palavras_chave if palavra in bloco.lower())
            blocos_pontuados.append((score, bloco))
        
        # Ordena pelos mais relevantes e pega os top N
        blocos_pontuados.sort(key=lambda x: x[0], reverse=True)
        contexto_selecionado = [bloco for score, bloco in blocos_pontuados[:self.num_passages]]

        
        previsao = self.gerar_resposta(
            contexto="\n\n".join(contexto_selecionado), 
            user_input=user_input
        )

        return dspy.Prediction(contexto=contexto_selecionado, resposta=previsao.resposta)

rag_sistema = RAG(passagens=carregar_textos_pdf("docs/CMNn 4.935.pdf"),num_passages=3)

# Essa função chama as funções 
def processar_mensagem(mensagem: str, message):
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
        return rag_sistema(user_input=mensagem).resposta

    # Pega a string da variável funcao_ou_classe_escolhida e vê se tem o nome certo dentro
    if "contratos_nao_elegiveis" in escolha:
        Contratos_nao_elegiveis(message)
    elif "contratos_elegiveis" in escolha:
        Contratos_elegiveis(message)
    elif "cumprimento_metas_chamar" in escolha:
        cumprimento_metas_chamar(message)
    elif "comissao_loja_chamar" in escolha:
        comissao_loja_chamar(message)
    elif "comissao_atendente_chamar" in escolha:
        comissao_atendente_chamar(message)
    elif "alerta_prazos" in escolha:
        alerta_prazos(message)
    else:
        return "Não entendi sua mensagem."

    return None

# Isso é só teste
if __name__=="__main__":
    mock_message = {"chat_id": 0} 
    
    print(processar_mensagem("Quem matou Osama Bin Laden?", mock_message))
    print(processar_mensagem("quero ver os contratos não elegiveis", mock_message))

# Essa linha verifica o raciocínio racional
dspy.inspect_history(n=1)
