import streamlit as st

st.set_page_config(
    page_title="Message Analyzer - PhishingHybridDetector",
    page_icon="📩",
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

# ─── SIDEBAR ────────────────────────────────────────
with st.sidebar:
    st.title("🛡️ PhishingHybridDetector")
    st.markdown("**Hybrid Phishing Detection**")
    st.markdown("---")
    st.markdown("### Modules")
    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/2_URL_Checker.py", label=" URL Checker", icon="🔗")
    st.page_link("pages/3_Behavior_Check.py", label=" Behavior Check", icon="🕵️")
    st.page_link("pages/4_Alerts_Dashboard.py", label=" Alerts Dashboard", icon="🚨")

    st.markdown("---")
    st.info("Analyze suspicious emails, SMS, WhatsApp messages")

    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ─── MAIN CONTENT ───────────────────────────────────
st.title("📩 Message / Text Analyzer")
st.markdown("Paste suspicious message content to extract indicators of phishing.")

col1, col2 = st.columns([3, 2])

with col1:
    message = st.text_area(
        "Enter message / email body / SMS content",
        height=220,
        placeholder="Dear Customer, Your account will be suspended in 24 hours unless you verify your details here: https://secure-login-verify.net/update ..."
    )

    if st.button("Analyze Message", type="primary", use_container_width=True):
        if not message.strip():
            st.warning("Please enter some text to analyze.")
        else:
            st.success("Analysis started... (placeholder result)")
            with st.expander("Detected Features", expanded=True):
                st.write("• Suspicious urgency language detected")
                st.write("• impersonation attempt (bank/customer service)")
                st.write("• 1 external link found")
                st.markdown("Confidence: **High risk** ⚠️")

with col2:
    st.subheader("Quick Statistics")
    st.metric("Messages Analyzed Today", "142", "+19")
    st.metric("Phishing Detected", "38", "+7", delta_color="inverse")
    st.progress(0.68)
    st.caption("Current model confidence threshold")

