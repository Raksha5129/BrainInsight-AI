import streamlit as st
from components.footer import show_footer

st.set_page_config(
    page_title="About BrainInsight",
    page_icon="🧠",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.image("assets/logo_with_text.png", width=420)

st.title("🧠 About BrainInsight")

st.write("""
BrainInsight is an AI-powered medical imaging application developed to
assist in the early detection of multiple neurological diseases from
MRI scans using Deep Learning.

The system provides automated prediction, disease information,
interactive analytics, and downloadable medical reports.
""")

st.divider()
st.subheader("📖 Project Overview")

st.info("""
BrainInsight utilizes an EfficientNetB0 Convolutional Neural Network
trained using Transfer Learning for multi-class brain disease
classification.

Supported Diseases:

• Alzheimer's Disease

• Brain Tumor

• Stroke

• Multiple Sclerosis

• Normal Brain
""")

st.divider()
st.subheader("💻 Technology Stack")

c1, c2 = st.columns(2)

with c1:

    st.success("""
### AI & Machine Learning

• TensorFlow

• Keras

• EfficientNetB0

• NumPy

• OpenCV
""")

with c2:

    st.success("""
### Development

• Python

• Streamlit

• Plotly

• Pandas

• ReportLab
""")

st.divider()
st.subheader("📊 Dataset")

st.write("""
Total MRI Images : **12,267**

Disease Classes : **5**

Image Size : **224 × 224**

Data Augmentation : Yes

Transfer Learning : EfficientNetB0
""")

st.divider()
st.subheader("✨ Features")

st.markdown("""
✅ AI Assisted MRI Diagnosis

✅ Multi-Class Brain Disease Detection

✅ Interactive Analytics Dashboard

✅ Disease Knowledge Library

✅ Confidence Visualization

✅ Probability Distribution Charts

✅ AI Summary

✅ Medical Recommendation

✅ Downloadable PDF Report

✅ Modern Interactive User Interface
""")

st.divider()
st.subheader("🚀 Future Scope")

st.write("""
• Grad-CAM Explainable AI

• Cloud Deployment

• Doctor Portal

• Patient History

• Multi-language Support

• DICOM Image Support

• Mobile Application

• Real-time Clinical Integration
""")

st.divider()
st.success("""
Developed as an AI-powered healthcare project for
multi-class brain disease detection using MRI scans.
""")
show_footer()