from backend.utils import is_ip_url, has_special_chars

def analyze_url(url):
    score = 0
    reasons = []

    if is_ip_url(url):
        score += 3
        reasons.append("IP-based URL")

    if has_special_chars(url):
        score += 2
        reasons.append("Suspicious characters in URL")

    if len(url) > 50:
        score += 1
        reasons.append("Long URL")

    risk = "Low"
    if score >= 4:
        risk = "High"
    elif score >= 2:
        risk = "Medium"

    return {
        "type": "url",
        "score": score,
        "risk": risk,
        "reasons": reasons
    }