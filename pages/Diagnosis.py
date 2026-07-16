import streamlit as st
import plotly.express as px
import pandas as pd

from utils.predictor import predict

from components.confidence_gauge import confidence_gauge
from components.progress_loader import show_progress
from components.ai_summary import show_ai_summary
from components.recommendation import show_recommendation
from components.disease_panel import show_disease_panel
from components.pdf_download import show_pdf_download
from components.footer import show_footer

# --------------------------------------------------

st.set_page_config(
    page_title="MRI Diagnosis",
    page_icon="assets/logo.png",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------

st.image("assets/logo_with_text.png", width=420)

st.title("🧠 MRI Diagnosis")

st.write(
    "Upload an MRI scan and let BrainInsight AI analyze it using the trained EfficientNetB0 model."
)

st.divider()

# ================= Upload ================= #

left, right = st.columns(2)

with left:

    st.subheader("📤 Upload MRI Scan")

    uploaded_file = st.file_uploader(
        "Choose MRI Image",
        type=["jpg", "jpeg", "png"]
    )

with right:

    st.subheader("🖼 MRI Preview")

    if uploaded_file:

        preview = predict(uploaded_file)

        with st.container(border=True):
            st.image(
                preview["image"],
                width=320
            )

    else:

        st.info("Image Preview will appear here.")

st.divider()

# ================= Analyze ================= #

if st.button("🚀 Analyze MRI", use_container_width=True):

    if uploaded_file is None:

        st.error("Please upload an MRI image first.")

    else:

        result = predict(uploaded_file)

        show_progress()

        st.success("✅ MRI analysis completed successfully.")

        st.divider()

        # ================= Result ================= #

        st.subheader("🧠 AI Diagnosis Result")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Prediction",
                result["prediction"]
            )

        with c2:

            st.metric(
                "Confidence",
                f"{result['confidence']:.2f}%"
            )

        with c3:

            if result["confidence"] >= 95:
                level = "High"

            elif result["confidence"] >= 80:
                level = "Medium"

            else:
                level = "Low"

            st.metric(
                "Confidence Level",
                level
            )

        st.divider()

        # ================= AI Summary ================= #

        show_ai_summary(result)

        st.divider()

        # ================= Confidence Gauge ================= #

        st.subheader("🎯 Model Confidence")

        gauge = confidence_gauge(result["confidence"])

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

        st.divider()

        # ================= Probability Chart ================= #

        df = pd.DataFrame({

            "Disease": list(result["probabilities"].keys()),

            "Probability": list(result["probabilities"].values())

        })

        fig = px.bar(

            df,

            x="Probability",

            y="Disease",

            orientation="h",

            color="Probability",

            color_continuous_scale="Blues",

            title="Prediction Probabilities"

        )

        fig.update_layout(
            height=450,
            template="plotly_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(
            family="Poppins",
            color="#1E293B"
            ),
        title_font=dict(
        size=22,
        color="#1E293B"
        )
        )

        st.plotly_chart(
           fig,
        use_container_width=True,
        config={"displayModeBar": False}
       )

        st.divider()

                # ================= Recommendation ================= #

        show_recommendation(result)

        st.divider()

        # ================= Disease Information ================= #

        info = show_disease_panel(result)

        st.divider()

        # ================= PDF Report ================= #

        show_pdf_download(result, info)

        st.divider()

        # ================= Medical Disclaimer ================= #

        st.warning("""
### ⚠ Medical Disclaimer

BrainInsight AI is an AI-assisted screening tool.

It is **not** a substitute for professional medical diagnosis.

Always consult a qualified neurologist or radiologist before making any medical decisions.
""")

# ================= Footer ================= #

show_footer()