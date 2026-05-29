from src.explainability.shap_explainer import ThreatExplainer
from src.inference.predictor import ThreatPredictor

predictor = ThreatPredictor()
explainer = ThreatExplainer()

sample = {}

for feature in predictor.features:
    sample[feature] = 0

result = explainer.explain(sample)

print("\nTop Features:\n")

for item in result:
    print(item)