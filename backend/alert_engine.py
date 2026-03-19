def generate_alert(nlp_result, url_result, behavior_result):
    total_score = (
        nlp_result["score"] +
        url_result["score"] +
        behavior_result["score"]
    )

    if total_score >= 8:
        alert = "🚨 HIGH RISK: Likely phishing attempt!"
    elif total_score >= 4:
        alert = "⚠️ MEDIUM RISK: Be cautious."
    else:
        alert = "✅ LOW RISK: Probably safe."

    return {
        "total_score": total_score,
        "final_alert": alert
    }