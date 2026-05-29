from langchain_ollama import ChatOllama

from src.rag.retriever import retrieve_context


class ThreatAnalyzer:

    def __init__(self):

        self.llm = ChatOllama(
            model="tinyllama",
            temperature=0.2
        )

    def analyze(
        self,
        attack_type: str,
        confidence: float
    ):

        context = retrieve_context(
            attack_type
        )

        prompt = f"""
You are a senior SOC analyst.

Attack Type:
{attack_type}

Confidence:
{confidence}

Threat Intelligence:
{context}

Generate:

1. Executive Summary
2. Risk Level
3. MITRE ATT&CK Mapping
4. Recommended Actions
"""

        response = self.llm.invoke(
            prompt
        )

        return response.content