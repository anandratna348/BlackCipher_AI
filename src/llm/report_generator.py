from datetime import datetime


def generate_report(
    prediction: dict,
    analysis: str
):

    return {
        "timestamp": datetime.utcnow().isoformat(),

        "prediction": {
            "attack_type": prediction["attack_type"],
            "confidence": prediction["confidence"],
            "model": prediction["model"]
        },

        "analysis": analysis
    }