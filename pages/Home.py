import streamlit as st
from components.footer import show_footer

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="BrainInsight AI",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Load CSS ---------------- #

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #

col1, col2, col3 = st.sidebar.columns([1, 2, 1])

with col2:
    st.image("assets/logo.png", width=120)

st.sidebar.markdown(
    "<h3 style='text-align:center;'>BrainInsight AI</h3>",
    unsafe_allow_html=True
)

st.sidebar.caption(
    "<p style='text-align:center;'>AI Powered MRI Diagnosis</p>",
    unsafe_allow_html=True
)

st.sidebar.markdown("---")
st.sidebar.markdown("---")

st.sidebar.success("Deep Learning MRI Analysis")

with st.sidebar.container(border=True):

    st.markdown("### 📋 Project Information")

    st.markdown("""
🧠 **Model:** EfficientNetB0

📊 **Accuracy:** 98.94%

📂 **Dataset:** 12,267 Images

🩺 **Diseases:** 5 Classes

⚡ **Framework:** TensorFlow
""")

st.sidebar.markdown("---")
st.sidebar.caption("BrainInsight AI © 2026")

# ---------------- Logo ---------------- #

st.image("assets/logo_with_text.png", width=500)

st.write("")

# ---------------- Hero Banner ---------------- #

st.image("assets/hero.png", use_container_width=True)

st.write("")

st.info("""
🧠 **Ready to analyze an MRI scan?**

Upload an MRI image and receive:
- AI-powered disease prediction
- Confidence score
- Disease information
- Downloadable PDF report
""")

if st.button("🚀 Start Diagnosis", use_container_width=True):
    st.switch_page("pages/Diagnosis.py")

st.write("")
st.write("")
# ---------------- Metrics ---------------- #

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🎯 Validation Accuracy",
        "98.94%"
    )

with c2:
    st.metric(
        "🧠 Disease Classes",
        "5"
    )

with c3:
    st.metric(
        "🖼 MRI Dataset",
        "12,267"
    )

with c4:
    st.metric(
        "🤖 AI Model",
        "EfficientNetB0"
    )

st.divider()

# ---------------- About ---------------- #

st.markdown("""
# Welcome to BrainInsight AI

BrainInsight AI is an intelligent deep learning platform developed for automated multi-class brain disease detection using MRI scans.

The system utilizes the EfficientNetB0 Convolutional Neural Network to classify MRI images into five neurological conditions with high accuracy, providing fast AI-assisted diagnosis and downloadable medical reports.
""")

st.divider()

# ---------------- Supported Diseases ---------------- #

st.markdown("## 🧠 Supported Diseases")

d1, d2, d3, d4, d5 = st.columns(5)

with d1:
    st.success("🧠\n\nAlzheimer's")

with d2:
    st.error("🧠\n\nBrain Tumor")

with d3:
    st.warning("🩸\n\nStroke")

with d4:
    st.info("🧬\n\nMultiple\nSclerosis")

with d5:
    st.success("✅\n\nNormal")

st.divider()

# ---------------- Feature Cards ---------------- #

st.markdown("## 🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### 🧠 AI Diagnosis

• Upload MRI Scan

• Automatic Disease Detection

• High Prediction Accuracy

• Fast Analysis
""")

with col2:

    st.success("""
### 🤖 AI Analysis

• Confidence Score

• Probability Distribution

• Disease Information

• Medical Recommendation
""")

with col3:

    st.warning("""
### 📄 Smart Reports

• Professional PDF

• Diagnosis Summary

• Treatment Information

• Download Report
""")

st.divider()

# ---------------- Workflow ---------------- #

st.markdown("## ⚙️ How BrainInsight Works")

w1, w2, w3, w4 = st.columns(4)

with w1:
    st.info("""
### 📤 Upload

Upload an MRI scan.
""")

with w2:
    st.info("""
### 🧹 Preprocess

Image resizing and normalization.
""")

with w3:
    st.info("""
### 🤖 AI Prediction

EfficientNetB0 analyzes the MRI.
""")

with w4:
    st.info("""
### 📄 Report

View results and download PDF.
""")

st.divider()

# ---------------- Technology ---------------- #

st.markdown("## 💻 Technology Stack")

t1, t2, t3, t4, t5, t6 = st.columns(6)

t1.metric("Framework", "TensorFlow")
t2.metric("Language", "Python")
t3.metric("Model", "EfficientNetB0")
t4.metric("Library", "OpenCV")
t5.metric("Frontend", "Streamlit")
t6.metric("Charts", "Plotly")

st.divider()

# ---------------- CTA ---------------- #

st.markdown("""
## 🩺 Ready to Diagnose?

Navigate to the **Diagnosis** page from the sidebar, upload an MRI scan and receive an AI-assisted diagnosis within seconds.
""")

st.success("✅ BrainInsight AI is Ready for Analysis")

st.write("")


show_footer()