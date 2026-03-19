def analyze_behavior(clicks_unknown_links: bool,
                     shares_sensitive_info: bool,
                     downloads_unknown_files: bool):
    
    score = 0
    issues = []

    if clicks_unknown_links:
        score += 2
        issues.append("Clicks unknown links")

    if shares_sensitive_info:
        score += 3
        issues.append("Shares sensitive information")

    if downloads_unknown_files:
        score += 2
        issues.append("Downloads unknown files")

    risk_level = "Low"
    if score >= 5:
        risk_level = "High"
    elif score >= 3:
        risk_level = "Medium"

    return {
        "score": score,
        "risk_level": risk_level,
        "issues": issues
    }