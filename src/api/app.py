from fastapi import FastAPI
from src.inference.predictor import ThreatPredictor
from src.llm.analyzer import ThreatAnalyzer
from src.llm.report_generator import generate_report
from src.explainability.shap_explainer import ThreatExplainer
from src.intelligence.mitre_mapper import get_mitre_mapping

app = FastAPI(
    title="BlackCipher AI",
    version="1.0.0"
)

predictor = ThreatPredictor()
analyzer = ThreatAnalyzer()
explainer = ThreatExplainer()


@app.get("/")
def root():
    return {
        "message": "BlackCipher AI Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(payload: dict):

    prediction = predictor.predict(payload)

    explanation = explainer.explain(payload)

    mitre = get_mitre_mapping(
        prediction["attack_type"]
    )

    analysis = analyzer.analyze(
        prediction["attack_type"],
        prediction["confidence"]
    )

    report = generate_report(
        prediction,
        analysis
    )

    report["mitre"] = mitre

    report["top_features"] = explanation

    return report