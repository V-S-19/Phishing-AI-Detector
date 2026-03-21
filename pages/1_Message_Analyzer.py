import streamlit as st
from backend.nlp_detector import analyze_message
from backend.alert_engine import generate_alert
from models.predict import predict_text

st.set_page_config(
    page_title="Message Analyzer - PhishingHybridDetector",
    page_icon="📩",
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
            with st.spinner("Analyzing message..."):
                single_result = analyze_message(message)
                final_alert = generate_alert([single_result])
                ml_result = predict_text(message)

            rule_level = final_alert["alert_level"]
            rule_score = final_alert["total_score"]

            # Hybrid final decision
            if ml_result == "Phishing Message" and rule_score >= 3:
                hybrid_level = "🚨 HIGH ALERT"
                hybrid_color_box = "error"
            elif ml_result == "Phishing Message" or rule_score >= 3:
                hybrid_level = "⚠️ MEDIUM ALERT"
                hybrid_color_box = "warning"
            elif rule_score >= 1:
                hybrid_level = "🟡 LOW ALERT"
                hybrid_color_box = "info"
            else:
                hybrid_level = "✅ SAFE"
                hybrid_color_box = "success"

            # Final result
            st.markdown("### 🔍 Final Hybrid Decision")
            if hybrid_color_box == "error":
                st.error(hybrid_level)
            elif hybrid_color_box == "warning":
                st.warning(hybrid_level)
            elif hybrid_color_box == "info":
                st.info(hybrid_level)
            else:
                st.success(hybrid_level)

            st.metric("Total Risk Score", rule_score)

            # Breakdown
            st.markdown("### 📊 Analysis Breakdown")
            st.write(f"**Rule-Based Alert:** {rule_level}")
            st.write(f"**ML Prediction:** {ml_result}")

            with st.expander("Detected Features", expanded=True):
                for item in final_alert["details"]:
                    r = item["risk"]
                    reason_str = ", ".join(item["reasons"]) if item["reasons"] else "no specific reason"
                    st.markdown(f"• **{item['type'].title()}**: {r} (score {item['score']}) → {reason_str}")

with col2:
    st.subheader("Quick Statistics")
    st.metric("Messages Analyzed Today", "142", "+19")
    st.metric("Phishing Detected", "38", "+7", delta_color="inverse")
    st.progress(0.68)
    st.caption("Current model confidence threshold")