from fastapi import FastAPI

from src.inference.predictor import ThreatPredictor

app = FastAPI(
    title="BlackCipher AI",
    version="1.0"
)

predictor = ThreatPredictor()

@app.get("/")
def root():

    return {
        "service": "BlackCipher AI",
        "status": "running"
    }
@app.get("/health")
def health():

    return {
        "status": "healthy"
    }