import os
import joblib

base_dir = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(base_dir, "text_model.pkl"))
vectorizer = joblib.load(os.path.join(base_dir, "vectorizer.pkl"))

def predict_text(message):
    X = vectorizer.transform([message])
    prediction = model.predict(X)[0]

    if prediction == 1:
        return "Phishing Message"
    return "Safe Message"