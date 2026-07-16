import streamlit as st

from utils.disease_info import DISEASE_INFO
from components.footer import show_footer
 
# --------------------------------------------------

st.set_page_config(
    page_title="Disease Library",
    page_icon="📚",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------

st.image("assets/logo_with_text.png", width=420)

st.title("📚 Brain Disease Library")

st.write(
    "Explore detailed information about the neurological diseases supported by BrainInsight AI."
)

st.divider()

# --------------------------------------------------

disease = st.selectbox(
    "🧠 Select Disease",
    list(DISEASE_INFO.keys())
)

info = DISEASE_INFO[disease]


st.divider()

# --------------------------------------------------
# Quick Facts
# --------------------------------------------------

st.subheader("📊 Quick Facts")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Disease", disease)

with c2:
    st.metric("Category", "Neurological")

with c3:
    st.metric("Severity", info.get("severity", "N/A"))

with c4:
    st.metric("AI Detection", "Supported")

st.divider()

# --------------------------------------------------
# Overview
# --------------------------------------------------

st.subheader("📖 Overview")

st.info(info.get("overview", "Overview not available."))

st.divider()

# --------------------------------------------------
# Symptoms & Risk Factors
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("⚠️ Symptoms")

    symptoms = info.get("symptoms", [])

    if symptoms:
        for symptom in symptoms:
            st.markdown(f"✅ {symptom}")
    else:
        st.info("No information available.")

with col2:

    st.subheader("📈 Risk Factors")

    risk_factors = info.get("risk_factors", [])

    if risk_factors:
        for risk in risk_factors:
            st.markdown(f"⚠️ {risk}")
    else:
        st.info("No information available.")

# --------------------------------------------------
# Causes
# --------------------------------------------------

st.subheader("🧬 Causes")

causes = info.get("causes", [])

if causes:
    for cause in causes:
        st.markdown(f"🧬 {cause}")
else:
    st.info("No information available.")

# --------------------------------------------------
# Treatment
# --------------------------------------------------

st.subheader("💊 Treatment")

treatment = info.get("treatment", [])

if isinstance(treatment, list):
    if treatment:
        for item in treatment:
            st.markdown(f"💊 {item}")
    else:
        st.info("No information available.")
else:
    st.success(treatment if treatment else "No information available.")

# --------------------------------------------------
# Prevention
# --------------------------------------------------

st.subheader("🩺 Prevention")

prevention = info.get("prevention", [])

if prevention:
    for item in prevention:
        st.markdown(f"✔️ {item}")
else:
    st.info("No information available.")

# --------------------------------------------------
# AI Detection
# --------------------------------------------------

st.subheader("🤖 How BrainInsight AI Detects This Disease")

st.info(info.get("ai_detection", "Information not available."))
st.divider()

# --------------------------------------------------
# Did You Know
# --------------------------------------------------

st.subheader("💡 Did You Know?")

st.info(info.get("did_you_know", "Information not available."))

st.divider()
 
# --------------------------------------------------
# References
# --------------------------------------------------

st.subheader("📚 References")

references = info.get("references", [])

if references:
    for ref in references:
        st.markdown(f"🔗 {ref}")
else:
    st.info("No references available.")
# --------------------------------------------------
# Medical Disclaimer
# --------------------------------------------------

st.warning("""
### ⚠ Medical Disclaimer

The information presented in this Disease Library is intended only for educational purposes.

BrainInsight AI is an AI-assisted screening tool and **must not replace professional medical diagnosis or treatment.**

Always consult a qualified neurologist or healthcare professional for medical advice.
""")

# --------------------------------------------------

show_footer()