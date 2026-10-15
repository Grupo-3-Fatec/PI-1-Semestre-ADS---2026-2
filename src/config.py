import dspy

#Esse é a função de configuração padrão pra todos os códigos que usam dspy
def lm_config(model="gemma4:e2b"):
    gemma4 = dspy.LM(
    model="ollama/gemma4:e2b",
    api_key="ollama",
    temperature=0.7,
    )
    dspy.configure(lm=gemma4)
    return gemma4
