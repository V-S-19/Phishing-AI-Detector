import streamlit as st
from datetime import datetime

# ─── Page Configuration ─────────────────────────────────────────────
st.set_page_config(
    page_title="PhishingHybridDetector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# ─── Hide ONLY the right side (Deploy button + 3 dots) ─────────────
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

# ─── Button Styling ─────────────────────────────────────────────────
st.markdown("""
    <style>
    .stButton > button[kind="primary"] {
        background-color: #d32f2f;
        color: white;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #b71c1c;
    }
    div.block-container {
        padding-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)



# ─── SIDEBAR ────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🛡️ PhishingHybridDetector")
    st.markdown("**Hybrid Phishing Detection**")
    st.markdown("---")
    
    st.markdown("### Modules")
    st.page_link("pages/1_Message_Analyzer.py", label=" Message Analyzer", icon="📩")
    st.page_link("pages/2_URL_Checker.py", label=" URL Checker", icon="🔗")
    st.page_link("pages/3_Behavior_Check.py", label=" Behavior Check", icon="🕵️")
    st.page_link("pages/4_Alerts_Dashboard.py", label=" Alerts Dashboard", icon="🚨")

    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)


# ─── MAIN CONTENT ───────────────────────────────────────────────────
st.title("🛡️ PhishingHybridDetector")
st.subheader("Protect yourself from phishing with hybrid analysis")

st.markdown("""
**PhishingHybridDetector** combines multiple detection techniques to identify suspicious content more reliably than single-method tools.
""")

st.divider()

st.subheader("Start Analysis")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📩 Analyze Message", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Message_Analyzer.py")

with col2:
    if st.button("🔗 Check URL", use_container_width=True, type="primary"):
        st.switch_page("pages/2_URL_Checker.py")

with col3:
    if st.button("🕵️ Behavior Check", use_container_width=True, type="primary"):
        st.switch_page("pages/3_Behavior_Check.py")

with col4:
    if st.button("🚨 Alerts Dashboard", use_container_width=True, type="primary"):
        st.switch_page("pages/4_Alerts_Dashboard.py")

st.divider()

st.subheader("At a Glance")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Analyses Today", "214", "+53")

with c2:
    st.metric("High-Risk Detections", "41", delta="+9", delta_color="inverse")

with c3:
    st.metric("Average Risk Score", "78%", "↓ 2%")

st.markdown("---")

with st.expander("How does it work?", expanded=False):
    st.markdown("""
    1. **Message Analyzer** → scans text for urgency, impersonation, suspicious patterns  
    2. **URL Checker** → evaluates domain age, reputation, typosquatting, blacklists  
    3. **Behavior Check** → looks for impossible travel, new devices, abnormal timing  
    4. **Alerts Dashboard** → shows recent detections and trends  
    """)

st.caption("Lightweight • No login required • Local-first analysis")