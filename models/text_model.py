import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train_text_model(path):
    df = pd.read_csv(
        path,
        sep="\t",
        header=None,
        names=["label", "message"],
        encoding="latin-1"
    )

    df["label"] = df["label"].map({"ham": 0, "spam": 1})

    extra_data = pd.DataFrame({
        "message": [
            "your account will be blocked click immediately",
            "verify your bank account now",
            "urgent action required login now",
            "your paypal account is suspended",
            "click here to avoid account suspension",
            "confirm your identity immediately",
            "your account has been compromised login now",
            "security alert verify your credentials",
            "reset your password now to avoid deactivation",
            "bank notice your account is locked"
        ],
        "label": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    })

    df = pd.concat([df[["message", "label"]], extra_data], ignore_index=True)

    X = df["message"]
    y = df["label"]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=5000
    )

    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    )

    model.fit(X_vec, y)

    return model, vectorizer