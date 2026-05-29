from src.inference.predictor import ThreatPredictor

predictor = ThreatPredictor()

sample = {
    "proto": "tcp",
    "state": "CON",
    "service": "http",
    "sport": "443",
    "dsport": "80",
    "ct_ftp_cmd": "0"
}

result = predictor.predict(sample)

print(result)