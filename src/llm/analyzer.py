from langchain_ollama import ChatOllama

from src.rag.retriever import retrieve_context


class ThreatAnalyzer:

    def __init__(self):

        self.llm = ChatOllama(
            model="tinyllama",
            temperature=0.1
        )

    def analyze(
        self,
        attack_type: str,
        confidence: float
    ):

        # Handle benign traffic without LLM
        if attack_type.lower() == "normal":

            return """
Executive Summary:
Traffic appears benign and no malicious activity was detected.

Risk Level:
Low

MITRE ATT&CK Mapping:
None

Recommended Actions:
- Continue routine monitoring
- Maintain current security controls
- Review logs periodically
- No immediate remediation required
"""

        context = retrieve_context(
            attack_type
        )

        prompt = f"""
You are a senior SOC analyst.

Analyze ONLY the attack type provided.

Attack Type:
{attack_type}

Model Confidence:
{confidence:.4f}

Threat Intelligence Context:
{context}

Rules:
- Use only the supplied attack type.
- Do not discuss unrelated attacks.
- Do not invent indicators or techniques.
- Keep response concise and professional.
- Maximum 200 words.

Generate exactly these sections:

Executive Summary:
(2-3 sentences)

Risk Level:
(Low/Medium/High/Critical)

MITRE ATT&CK Mapping:
(Technique name if available)

Recommended Actions:
(3-5 bullet points)
"""

        response = self.llm.invoke(
            prompt
        )

        return response.content