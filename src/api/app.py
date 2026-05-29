from fastapi import FastAPI

from src.inference.predictor import ThreatPredictor
from src.llm.analyzer import ThreatAnalyzer
from src.llm.report_generator import generate_report

app = FastAPI(
    title="BlackCipher AI",
    version="1.0.0"
)

predictor = ThreatPredictor()
analyzer = ThreatAnalyzer()


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

    prediction = predictor.predict(
        payload
    )

    analysis = analyzer.analyze(
        prediction["attack_type"],
        prediction["confidence"]
    )

    report = generate_report(
        prediction,
        analysis
    )

    return report