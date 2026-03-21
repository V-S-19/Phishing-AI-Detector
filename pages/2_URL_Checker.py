import streamlit as st
import re
from urllib.parse import urlparse

st.set_page_config(
    page_title="URL Checker - PhishingHybridDetector",
    page_icon="🔗",
    layout="wide"
)

hide_right_header = """
    <style>
    .stAppDeployButton { display: none !important; }
    #MainMenu { visibility: hidden; }
    header[data-testid="stHeader"] { visibility: visible; }
    </style>
"""
st.markdown(hide_right_header, unsafe_allow_html=True)


def analyze_url(url):
    score = 0
    reasons = []

    original_url = url.strip()
    url = original_url.lower()

    if not url:
        return {
            "alert_level": "SAFE",
            "total_score": 0,
            "details": [{
                "type": "url",
                "risk": "Low",
                "score": 0,
                "reasons": ["No URL provided"]
            }]
        }

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    suspicious_words = [
        "login", "verify", "update", "secure", "account",
        "bank", "paypal", "confirm", "signin", "password",
        "reset", "wallet", "suspended", "unlock"
    ]

    suspicious_tlds = [".tk", ".ru", ".xyz", ".top", ".gq", ".ml", ".cf"]

    # 1. HTTP instead of HTTPS
    if parsed.scheme == "http":
        score += 2
        reasons.append("Uses HTTP instead of HTTPS")

    # 2. IP address instead of domain
    if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", domain):
        score += 3
        reasons.append("Uses IP address instead of domain name")

    # 3. Suspicious keywords
    found_words = [word for word in suspicious_words if word in url]
    if found_words:
        score += min(len(found_words), 3)
        reasons.append(f"Suspicious keywords found: {', '.join(found_words)}")

    # 4. Too many hyphens
    if domain.count("-") >= 2:
        score += 2
        reasons.append("Too many hyphens in domain")

    # 5. Very long URL
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    # 6. Suspicious TLD
    for tld in suspicious_tlds:
        if domain.endswith(tld):
            score += 2
            reasons.append(f"Suspicious domain extension: {tld}")
            break

    # 7. @ trick
    if "@" in url:
        score += 3
        reasons.append("Contains @ symbol, possible redirection trick")

    # 8. Too many subdomains
    if len(domain.split(".")) > 3:
        score += 1
        reasons.append("Too many subdomains")

    # 9. Suspicious path words
    suspicious_path_words = ["login", "verify", "update", "confirm", "reset", "signin"]
    path_hits = [word for word in suspicious_path_words if word in path]
    if path_hits:
        score += 1
        reasons.append(f"Suspicious path content: {', '.join(path_hits)}")

    # Final classification
    if score >= 5:
        alert_level = "HIGH ALERT"
        risk = "High"
    elif score >= 2:
        alert_level = "MEDIUM ALERT"
        risk = "Medium"
    else:
        alert_level = "SAFE"
        risk = "Low"

    return {
        "alert_level": alert_level,
        "total_score": score,
        "details": [{
            "type": "url",
            "risk": risk,
            "score": score,
            "reasons": reasons if reasons else ["No major suspicious indicators found"]
        }]
    }


with st.sidebar:
    st.title("🛡️ PhishingHybridDetector")
    st.markdown("**Hybrid Phishing Detection**")
    st.markdown("---")
    st.markdown("### Modules")
    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/1_Message_Analyzer.py", label=" Message Analyzer", icon="📩")
    st.page_link("pages/3_Behavior_Check.py", label=" Behavior Check", icon="🕵️")
    st.page_link("pages/4_Alerts_Dashboard.py", label=" Alerts Dashboard", icon="🚨")
    st.markdown("---")
    st.markdown("## 🔗 URL / Domain Checker")
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔗 URL Checker")
st.markdown("Check whether a URL or domain looks safe or suspicious.")

url = st.text_input(
    "Paste URL / Link here",
    placeholder="https://example.com/login"
)

if st.button("Check URL", type="primary", use_container_width=True):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        result = analyze_url(url)
        level = result["alert_level"]

        if "HIGH" in level:
            st.error(f"🚨 {level}")
        elif "MEDIUM" in level:
            st.warning(f"⚠️ {level}")
        else:
            st.success(f"✅ {level}")

        st.metric("Risk Score", result["total_score"])

        with st.expander("Detailed Report", expanded=True):
            for item in result["details"]:
                reason_str = ", ".join(item["reasons"]) if item["reasons"] else "No specific reason"
                st.markdown(f"• **{item['type'].title()}**: {item['risk']} (score {item['score']})")
                st.markdown(f"  {reason_str}")