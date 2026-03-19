import streamlit as st

st.set_page_config(
    page_title="Behavior Check - PhishingHybridDetector",
    page_icon="🕵️",
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
    st.page_link("pages/3_Behavior_Check.py", label=" Behavior Check", icon="🕵️")
    st.page_link("pages/4_Alerts_Dashboard.py", label=" Alerts Dashboard", icon="🚨")
    st.markdown("---")
    st.title("🕵️ Behavioral & Contextual Analysis")
    st.markdown("Analyze login attempts, session behavior, timing, etc.")

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
        ip = st.text_input("IP Address", "103.XX.XX.47")
        user_agent = st.text_input("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...")
        timezone = st.selectbox("Reported Timezone", ["Asia/Kolkata", "Europe/London", "America/New_York"])

    with col2:
        st.subheader("Behavior Flags")
        if st.button("Run Behavior Check", type="primary"):
            st.info("Analyzing...")
            st.write("• Login from new country → **suspicious**")
            st.write("• Very short session duration (< 8s)")
            st.write("• Rapid page transitions detected")
            st.error("**Possible credential stuffing / session hijacking**")

with tab2:
    st.info("Upload CSV / JSON of multiple login attempts (coming soon)")
    st.caption("Future feature: bulk behavioral scoring")