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

        df = df[self.features]

        prediction = self.model.predict(df)

        attack_type = self.encoder.inverse_transform(
            prediction
        )[0]

        return attack_type