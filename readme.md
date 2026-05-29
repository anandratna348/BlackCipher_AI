# BlackCipher AI

## AI-Powered Cyber Threat Intelligence Platform

BlackCipher AI is an end-to-end cyber threat detection and analysis platform that combines Machine Learning, Explainable AI, Retrieval-Augmented Generation (RAG), MITRE ATT&CK Mapping, and Local LLMs to provide actionable security insights from network traffic.

The platform is built using the UNSW-NB15 dataset and is capable of detecting multiple attack categories, explaining predictions, retrieving threat intelligence, and generating SOC-style incident reports.

---

## Features

### Network Intrusion Detection

* XGBoost-based multiclass intrusion detection model
* Trained on UNSW-NB15 dataset
* Detects multiple attack categories including:

  * Exploits
  * DoS
  * Reconnaissance
  * Fuzzers
  * Worms
  * Backdoor
  * Shellcode
  * Generic
  * Normal Traffic

### Explainable AI

* SHAP-based feature importance analysis
* Explains why a prediction was made
* Identifies top contributing network features

### Threat Intelligence (RAG)

* FAISS vector database
* Local cybersecurity knowledge base
* Context retrieval for detected threats
* Retrieval-Augmented Generation pipeline

### LLM-Powered SOC Analysis

* TinyLlama integration via Ollama
* Generates security analyst reports
* Executive summaries
* Risk assessment
* Recommended actions

### MITRE ATT&CK Mapping

* Maps attacks to MITRE ATT&CK techniques
* Provides severity classification
* Enhances threat context

### FastAPI Backend

* REST API endpoints
* Swagger documentation
* Real-time analysis

---

## Architecture

Network Traffic

↓

XGBoost Threat Detection

↓

SHAP Explainability

↓

MITRE ATT&CK Mapping

↓

FAISS RAG Retrieval

↓

TinyLlama Analysis

↓

SOC Incident Report

---

## Tech Stack

### Machine Learning

* Python
* XGBoost
* Scikit-Learn
* Pandas
* NumPy

### Explainability

* SHAP

### RAG Pipeline

* LangChain
* FAISS
* Sentence Transformers

### LLM

* Ollama
* TinyLlama

### API

* FastAPI
* Uvicorn

### Version Control

* Git
* GitHub

---

## Project Structure

```text
BlackCipher_AI/

├── models/
│   ├── xgb_base_model.pkl
│   ├── xgb_smote_model.pkl
│   ├── target_encoder.pkl
│   ├── feature_columns.pkl
│   └── feature_encoders.pkl
│
├── knowledgebase/
│   ├── exploits.md
│   ├── dos.md
│   ├── reconnaissance.md
│   └── mitre_attack.md
│
├── vectorstore/
│
├── src/
│   ├── api/
│   │   └── app.py
│   │
│   ├── inference/
│   │   └── predictor.py
│   │
│   ├── explainability/
│   │   └── shap_explainer.py
│   │
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   │
│   ├── llm/
│   │   ├── analyzer.py
│   │   └── report_generator.py
│   │
│   ├── intelligence/
│   │   └── mitre_mapper.py
│   │
│   └── schemas/
│
└── tests/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/BlackCipher_AI.git

cd BlackCipher_AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull TinyLlama:

```bash
ollama pull tinyllama
```

Verify:

```bash
ollama list
```

---

## Build Vector Database

```bash
python -m src.rag.ingest
```

---

## Run API

```bash
uvicorn src.api.app:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Example Request

```json
{
  "proto": "tcp",
  "state": "CON",
  "service": "http",
  "sport": "443",
  "dsport": "80",
  "ct_ftp_cmd": "0"
}
```

---

## Example Response

```json
{
  "timestamp": "2026-05-29T16:58:39",
  "prediction": {
    "attack_type": "Normal",
    "confidence": 0.9924,
    "model": "xgb_base_model"
  },
  "mitre": {
    "technique": "None",
    "name": "Benign Traffic",
    "severity": "Low"
  },
  "top_features": [
    {
      "feature": "sttl",
      "importance": 0.78437
    }
  ],
  "analysis": "Traffic appears benign and no malicious activity was detected."
}
```

---

## Dataset

UNSW-NB15 Dataset

The dataset contains modern network traffic and attack scenarios used for intrusion detection research.

Attack Categories:

* Analysis
* Backdoor
* DoS
* Exploits
* Fuzzers
* Generic
* Reconnaissance
* Shellcode
* Worms
* Normal

---

## Future Enhancements

* PDF Incident Report Generation
* Real-Time Traffic Monitoring
* Security Dashboard
* Docker Deployment
* Kubernetes Deployment
* Multi-LLM Support
* Threat History Database
* SIEM Integration

---
