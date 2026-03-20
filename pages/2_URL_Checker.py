import streamlit as st
from backend.url_analyzer import analyze_url
from backend.alert_engine import generate_alert

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
    st.title("🔗 URL / Domain Checker")
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

url = st.text_input("Paste URL / Link here", placeholder="https://example-login-secure.com/update-password")

if st.button("Check URL", type="primary", use_container_width=True):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        with st.spinner("Analyzing URL..."):
            # ── Real analysis ─────────────────────────────────────
            result = analyze_url(url)
            alert = generate_alert([result])

        # ── Show result ───────────────────────────────────────────
        level = alert["alert_level"]
        emoji = "✅" if "SAFE" in level else "⚠️" if "MEDIUM" in level else "🚨"

        st.markdown(f"### {emoji} **{level}**", unsafe_allow_html=True)
        st.metric("Risk Score", alert["total_score"])

        with st.expander("Detailed Report", expanded=True):
            for d in alert["details"]:
                reasons = ", ".join(d["reasons"]) if d["reasons"] else "no specific indicators"
                st.markdown(f"- **{d['type'].title()}**: {d['risk']} (score {d['score']})  \n  {reasons}")

st.caption("Last updated database: March 18, 2026")