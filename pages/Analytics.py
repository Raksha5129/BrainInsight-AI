import streamlit as st
import plotly.express as px
import pandas as pd
from components.footer import show_footer

st.set_page_config(
    page_title="BrainInsight Analytics",
    page_icon="📊",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.image("assets/logo_with_text.png", width=400)

st.title("📊 BrainInsight Analytics")

st.write(
    """
Monitor AI model performance, dataset statistics,
and deployment information.
"""
)

st.divider()

# ================= KPI Cards ================= #

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🎯 Validation Accuracy",
        "98.94%"
    )

with c2:
    st.metric(
        "🧠 Diseases",
        "5"
    )

with c3:
    st.metric(
        "🖼 MRI Images",
        "12,267"
    )

with c4:
    st.metric(
        "🤖 Model",
        "EfficientNetB0"
    )

st.divider()
# ================= Dataset Distribution ================= #

st.subheader("📊 Dataset Distribution")

dataset = pd.DataFrame({
    "Disease": [
        "Alzheimer",
        "Tumor",
        "Multiple Sclerosis",
        "Normal",
        "Stroke"
    ],
    "Images": [
        4500,
        4200,
        1411,
        1400,
        756
    ]
})

col1, col2 = st.columns([1, 1])

with col1:

    fig = px.pie(
        dataset,
        names="Disease",
        values="Images",
        hole=0.45,
        title="MRI Dataset Distribution"
    )

    fig.update_traces(textposition="inside", textinfo="percent+label")

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.dataframe(
        dataset,
        use_container_width=True,
        hide_index=True
    )

st.divider()
# ================= Model Information ================= #

st.subheader("🧠 Model Information")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### 🤖 AI Model

- **Model:** EfficientNetB0
- **Framework:** TensorFlow 2.21
- **Technique:** Transfer Learning
- **Fine-Tuning:** Yes
- **Input Size:** 224 × 224 × 3
- **Output Classes:** 5
""")

with c2:

    st.success("""
### 📋 Training Configuration

- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy
- **Activation:** Softmax
- **Image Size:** 224 × 224
- **Dataset:** 12,267 MRI Images
- **Validation Accuracy:** 98.94%
""")
    

st.divider()
# ================= System Information ================= #

st.subheader("💻 Deployment Information")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### 🖥 Development Environment

- VS Code
- Python 3.12
- Streamlit
- TensorFlow 2.21
- Plotly
- Pandas
- NumPy
""")

with col2:

    st.markdown("""
### 🚀 BrainInsight AI

- Deep Learning Based Diagnosis
- Multi-Class MRI Classification
- AI Assisted Screening
- PDF Report Generation
- Interactive Dashboard
- Professional User Interface
""")

st.divider()
# ================= Project Summary ================= #

st.subheader("📈 Project Summary")

st.success("""
BrainInsight AI is a deep learning-based medical imaging application
designed to assist in the detection of multiple brain diseases from MRI scans.

The application integrates:

✅ EfficientNetB0 Transfer Learning Model

✅ Automated MRI Classification

✅ AI Generated Diagnosis Summary

✅ Confidence Visualization

✅ Interactive Analytics Dashboard

✅ Disease Information Library

✅ PDF Medical Report Generation

The current model has been trained on **12,267 MRI images**
covering **5 neurological conditions**.
""")
show_footer()