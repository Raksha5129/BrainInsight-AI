import streamlit as st


def show_ai_summary(result):

    st.subheader("🤖 AI Summary")

    st.info(f"""
The uploaded MRI scan is classified as **{result['prediction']}**
with a confidence of **{result['confidence']:.2f}%**.

The prediction is generated using the trained
**EfficientNetB0** deep learning model.

This result is intended for AI-assisted screening
and should always be interpreted by a qualified
medical professional.
""")