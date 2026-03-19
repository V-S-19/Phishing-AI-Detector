import re
from urllib.parse import urlparse
from backend.utils import is_suspicious_domain

def analyze_url(url: str):
    parsed = urlparse(url)

    score = 0
    reasons = []

    # Check HTTPS
    if parsed.scheme != "https":
        score += 1
        reasons.append("Not using HTTPS")

    # Suspicious domain keywords
    if is_suspicious_domain(url):
        score += 2
        reasons.append("Suspicious domain keywords")

    # IP address instead of domain
    if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc):
        score += 2
        reasons.append("IP address used instead of domain")

    # Long URL
    if len(url) > 75:
        score += 1
        reasons.append("URL is too long")

    risk_level = "Low"
    if score >= 4:
        risk_level = "High"
    elif score >= 2:
        risk_level = "Medium"

    return {
        "score": score,
        "risk_level": risk_level,
        "reasons": reasons
    }