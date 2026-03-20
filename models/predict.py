import joblib


model = joblib.load("models/text_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_text(message):
    X = vectorizer.transform([message])
    prediction = model.predict(X)[0]

    if prediction == 1:
        return "Phishing Message"
    return "Safe Message"