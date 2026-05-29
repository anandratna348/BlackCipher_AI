from src.inference.predictor import ThreatPredictor

predictor = ThreatPredictor()

sample = {}

for feature in predictor.features:
    sample[feature] = 0

result = predictor.predict(sample)

print(result)