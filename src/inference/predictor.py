
import joblib
import pandas as pd


class ThreatPredictor:

    def __init__(self):

        self.model = joblib.load(
            "models/xgb_base_model.pkl"
        )

        self.encoder = joblib.load(
            "models/target_encoder.pkl"
        )

        self.features = joblib.load(
            "models/feature_columns.pkl"
        )

    def predict(self, data: dict):

        df = pd.DataFrame([data])

        # Ensure correct feature order
        df = df[self.features]

        prediction = self.model.predict(df)

        probabilities = self.model.predict_proba(df)

        confidence = float(
            probabilities.max()
        )

        attack_type = self.encoder.inverse_transform(
            prediction
        )[0]

        return {
            "attack_type": str(attack_type),
            "confidence": round(confidence, 4),
            "model": "xgb_base_model"
        }