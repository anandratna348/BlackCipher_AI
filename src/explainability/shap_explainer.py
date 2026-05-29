import joblib
import shap
import pandas as pd
import numpy as np


class ThreatExplainer:

    def __init__(self):

        self.model = joblib.load(
            "models/xgb_base_model.pkl"
        )

        self.features = joblib.load(
            "models/feature_columns.pkl"
        )

        self.encoders = joblib.load(
            "models/feature_encoders.pkl"
        )

        self.explainer = shap.TreeExplainer(
            self.model
        )

    def explain(self, data: dict):

        df = pd.DataFrame([data])

        # Fill missing features
        for feature in self.features:

            if feature not in df.columns:
                df[feature] = 0

        # Apply encoders used during training
        for col, encoder in self.encoders.items():

            if col in df.columns:

                try:

                    df[col] = encoder.transform(
                        df[col].astype(str)
                    )

                except Exception:

                    df[col] = 0

        # Match training feature order
        df = df[self.features]

        shap_values = self.explainer.shap_values(
            df
        )

        shap_array = np.array(
            shap_values
        )

        print(
            "SHAP SHAPE:",
            shap_array.shape
        )

        # Handle multiclass XGBoost
        if len(shap_array.shape) == 3:

            # Example:
            # (1, 43, 14)
            # (14, 1, 43)

            if shap_array.shape[1] == len(
                self.features
            ):

                importance = np.mean(
                    np.abs(shap_array),
                    axis=(0, 2)
                )

            elif shap_array.shape[2] == len(
                self.features
            ):

                importance = np.mean(
                    np.abs(shap_array),
                    axis=(0, 1)
                )

            else:

                raise ValueError(
                    f"Unable to identify feature dimension: {shap_array.shape}"
                )

        elif len(shap_array.shape) == 2:

            importance = np.mean(
                np.abs(shap_array),
                axis=0
            )

        else:

            raise ValueError(
                f"Unexpected SHAP shape: {shap_array.shape}"
            )

        importance = np.ravel(
            importance
        )

        top_features = sorted(
            zip(
                self.features,
                importance.tolist()
            ),
            key=lambda x: float(x[1]),
            reverse=True
        )[:10]

        return [
            {
                "feature": str(feature),
                "importance": round(
                    float(score),
                    6
                )
            }
            for feature, score in top_features
        ]