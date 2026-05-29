from datetime import datetime


def generate_report(
    prediction: dict,
    analysis: str
):

    return {
        "timestamp": datetime.utcnow().isoformat(),

        "prediction": prediction,

        "analysis": analysis
    }