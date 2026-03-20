def analyze_behavior(clicks, time_spent, unknown_device):
    score = 0
    reasons = []

    if clicks > 3:
        score += 2
        reasons.append("Multiple suspicious clicks")

    if time_spent < 5:
        score += 1
        reasons.append("Very quick interaction")

    if unknown_device:
        score += 2
        reasons.append("Unknown device detected")

    risk = "Low"
    if score >= 4:
        risk = "High"
    elif score >= 2:
        risk = "Medium"

    return {
        "type": "behavior",
        "score": score,
        "risk": risk,
        "reasons": reasons
    }