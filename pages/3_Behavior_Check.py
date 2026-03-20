import streamlit as st
from backend.behavior_analyzer import analyze_behavior
from backend.alert_engine import generate_alert

st.set_page_config(
    page_title="Behavior Check - PhishingHybridDetector",
    page_icon="🕵️",
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
    st.page_link("pages/2_URL_Checker.py", label=" URL Checker", icon="🔗")
    st.page_link("pages/4_Alerts_Dashboard.py", label=" Alerts Dashboard", icon="🚨")
    st.markdown("---")
    st.title("🕵️ Behavioral & Contextual Analysis")

    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Single Session Check", "Multiple Events"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Session Information")
        ip = st.text_input("IP Address", "103.XX.XX.47")           # not used yet
        user_agent = st.text_input("User-Agent", "...")            # not used yet
        timezone = st.selectbox("Reported Timezone", ["Asia/Kolkata", "Europe/London", "America/New_York"])  # not used yet

    with col2:
        st.subheader("Behavior Flags")
        clicks = st.number_input("Number of suspicious clicks", min_value=0, value=0, step=1)
        time_spent = st.number_input("Session duration (seconds)", min_value=0.0, value=10.0, step=0.5)
        unknown_device = st.checkbox("Unknown / new device", value=False)

        if st.button("Run Behavior Check", type="primary"):
            with st.spinner("Analyzing behavior..."):
                result = analyze_behavior(clicks, time_spent, unknown_device)
                alert = generate_alert([result])

            level = alert["alert_level"]
            emoji = "✅" if "SAFE" in level else "⚠️" if "MEDIUM" in level else "🚨"

            st.markdown(f"### {emoji} **{level}** – score {alert['total_score']}")
            
            with st.expander("Details"):
                for item in alert["details"]:
                    st.write(f"• {', '.join(item['reasons'])}")

with tab2:
    st.info("Upload CSV / JSON of multiple login attempts (coming soon)")
    st.caption("Future feature: bulk behavioral scoring")