from src.llm.analyzer import ThreatAnalyzer

analyzer = ThreatAnalyzer()

result = analyzer.analyze(
    "Exploits",
    0.95
)

print(result)