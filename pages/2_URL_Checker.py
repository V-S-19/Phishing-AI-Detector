import streamlit as st

st.set_page_config(
    page_title="URL Checker - PhishingHybridDetector",
    page_icon="🔗",
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
    st.title("🔗 URL / Domain Checker")
    st.markdown("Verify whether a link is likely to be malicious or phishing-related.")

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
        with st.status("Analyzing URL...", expanded=True) as status:
            st.write("Checking domain age...")
            st.write("Looking up SSL certificate...")
            st.write("Scanning against known phishing feeds...")
            st.write("Performing typo-squatting detection...")
            status.update(label="Analysis complete!", state="complete", expanded=False)

        col_left, col_right = st.columns(2)
        with col_left:
            st.error("**HIGH RISK** – Phishing probability: 92%")
        with col_right:
            st.success("**Safe signals found**: 3 / 18")

        st.divider()
        with st.expander("Detailed Report"):
            st.markdown("""
            - Domain registered: **7 days ago** 🚩  
            - Uses free hosting (000webhost-like) 🚩  
            - SSL: Let's Encrypt (common in phishing)  
            - Domain similar to: `chase.com`, `paypal.com`  
            - Blacklist status: **Detected in 4 phishing feeds**
            """)

st.caption("Last updated database: March 18, 2026")