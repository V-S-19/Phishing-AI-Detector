import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Alerts Dashboard - PhishingHybridDetector",
    page_icon="🚨",
    layout="wide"
)

hide_right_header = """
    <style>
    /* Hide Deploy button */
    .stAppDeployButton {
        display: none !important;
    }
    /* Hide 3-dots menu */
    #MainMenu {
        visibility: hidden;
    }
    /* Keep the left header (logo + title) visible */
    header[data-testid="stHeader"] {
        visibility: visible;
    }
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
    st.page_link("pages/2_URL_Checker.py", label=" URL Checker", icon="🔗")
    st.page_link("pages/3_Behavior_Check.py", label=" Behavior Check", icon="🕵️")
    st.markdown("---")
    st.title("🚨 Alerts Dashboard")
    st.markdown("Real-time overview of phishing detections and high-risk events")

    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Fake recent alerts (you can later connect real data)
data = {
    "Time": ["10 min ago", "23 min ago", "47 min ago", "1.8 hr ago", "2.4 hr ago"],
    "Source": ["Email", "SMS", "URL", "Message", "URL"],
    "Risk": ["Critical", "High", "High", "Medium", "Critical"],
    "Target": ["PayPal", "SBI", "Office365", "WhatsApp", "Amazon"],
    "Score": [94, 87, 82, 68, 91]
}
df = pd.DataFrame(data)

col1, col2, col3 = st.columns(3)
col1.metric("Active Alerts", "17", "+4")
col2.metric("Critical Detections", "6", "+2", delta_color="inverse")
col3.metric("Avg. Confidence", "84%", "↑ 3%")

st.subheader("Recent Alerts")
st.dataframe(
    df.style.applymap(
        lambda v: "color: #b71c1c; font-weight:bold;" if v in ["Critical", 91, 94] else None,
        subset=["Risk", "Score"]
    ),
    use_container_width=True
)

st.subheader("Risk Trend (last 24 hours)")
# You can later replace with real chart
st.line_chart({"Detections": [3,5,8,12,9,14,19,22]}, height=180)

if st.button("Export Alerts (CSV)", disabled=True):
    st.info("Export functionality coming soon")