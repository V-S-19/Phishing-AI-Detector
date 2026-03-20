def generate_alert(results):
    total_score = sum(r["score"] for r in results)

    if total_score >= 7:
        level = "🚨 HIGH ALERT"
    elif total_score >= 4:
        level = "⚠️ MEDIUM ALERT"
    else:
        level = "✅ SAFE"

    return {
        "total_score": total_score,
        "alert_level": level,
        "details": results
    }