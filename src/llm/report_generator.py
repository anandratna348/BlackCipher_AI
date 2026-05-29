from datetime import datetime


def generate_report(
    attack_type,
    confidence,
    analysis
):

    return {
        "timestamp": str(
            datetime.utcnow()
        ),
        "attack_type": attack_type,
        "confidence": confidence,
        "analysis": analysis
    }