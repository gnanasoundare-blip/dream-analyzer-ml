# Dream Analyzer (ML)
A local ML model that classifies dream descriptions into themes.
Run: python analyze_dream.py --model model.pkl
Author: S Gnanasoundare

## 🧠 Overview
The **Dream Analyzer** is an intelligent Python-based project that interprets short dream descriptions and predicts their underlying *emotional themes* — such as *fear*, *freedom*, *nostalgia*, or *happiness*.

It uses a **Machine Learning model (TF-IDF + Logistic Regression)** trained on example dream data.  
The model learns how certain words and patterns correspond to common dream emotions, making it a foundation for emotional NLP experiments.

---

## ✨ Features
- 🧩 Text-based emotion classification  
- 🧠 Machine learning model built with scikit-learn  
- 🪄 Interactive dream analysis prompt  
- 📈 Extendable dataset for more accurate results  
- 💾 Saved `model.pkl` for reuse  

---

## ⚙️ Requirements
Make sure you have Python 3.9+ installed.  
Install dependencies using:

```bash
pip install -r requirements.txt
