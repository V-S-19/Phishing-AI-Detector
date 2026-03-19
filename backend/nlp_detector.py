from backend.utils import clean_text

PHISHING_KEYWORDS = [
    "urgent", "verify", "password", "click", "login",
    "bank", "account", "suspend", "security", "update"
]

def analyze_message(message: str):
    message = clean_text(message)

    score = 0
    found_keywords = []

    for word in PHISHING_KEYWORDS:
        if word in message:
            score += 1
            found_keywords.append(word)

    risk_level = "Low"
    if score >= 5:
        risk_level = "High"
    elif score >= 3:
        risk_level = "Medium"

    return {
        "score": score,
        "risk_level": risk_level,
        "keywords_found": found_keywords
    }