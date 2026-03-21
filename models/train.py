import joblib
from text_model import train_text_model


def main():
    print("Training started...")
    model, vectorizer = train_text_model("data/spam.csv")

    joblib.dump(model, "models/text_model.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")

    print("Model trained and saved successfully!")


if __name__ == "__main__":
    main()