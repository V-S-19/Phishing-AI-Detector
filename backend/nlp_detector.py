from backend.utils import contains_urgency, contains_suspicious_links

def analyze_message(message):
    score = 0
    reasons = []

    if contains_urgency(message):
        score += 2
        reasons.append("Urgency detected")

    if contains_suspicious_links(message):
        score += 2
        reasons.append("Contains link")

    if "bank" in message.lower() or "account" in message.lower():
        score += 1
        reasons.append("Impersonation attempt")
    risk = "Low"
    if score >= 4:
        risk = "High"
    elif score >= 2:
        risk = "Medium"

    return {
        "type": "message",
        "score": score,
        "risk": risk,
        "reasons": reasons
    }