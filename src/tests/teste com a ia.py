import dspy
import pandas as pd

dspy.configure(lm=dspy.LM(model="ollama/gemma4:e2b"))

def soma(a, b):
    """Essa funçao soma dois numeros"""
    return a + b

agent = dspy.ReAct(
    "question: str -> response: str",
    tools=[soma]
)

result = agent(
    question="quanto eh 2+2?"
)

print(result.response)