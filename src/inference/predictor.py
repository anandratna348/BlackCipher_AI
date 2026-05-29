import joblib
import pandas as pd


class ThreatPredictor:

    def __init__(self):

        self.model = joblib.load(
            "models/xgb_base_model.pkl"
        )

        self.target_encoder = joblib.load(
            "models/target_encoder.pkl"
        )

        self.features = joblib.load(
            "models/feature_columns.pkl"
        )

        self.encoders = joblib.load(
            "models/feature_encoders.pkl"
        )

    def predict(self, data: dict):

        df = pd.DataFrame([data])

        # Fill missing features
        for feature in self.features:

            if feature not in df.columns:

                df[feature] = 0

        # Apply categorical encoders
        for col, encoder in self.encoders.items():

            if col in df.columns:

                try:

                    df[col] = encoder.transform(
                        df[col].astype(str)
                    )

                except ValueError:

                    # Unknown category
                    df[col] = 0

        # Ensure feature order
        df = df[self.features]

        prediction = self.model.predict(df)

        probabilities = self.model.predict_proba(df)

        confidence = float(
            probabilities.max()
        )

        attack_type = self.target_encoder.inverse_transform(
            prediction
        )[0]

        return {
            "attack_type": str(attack_type),
            "confidence": round(confidence, 4),
            "model": "xgb_base_model"
        }