import streamlit as st
from utils.disease_info import DISEASE_INFO


def show_disease_panel(result):

    st.subheader("📚 Disease Information")

    info = DISEASE_INFO[result["prediction"]]

    with st.expander("📖 Overview", expanded=True):
        st.write(info["overview"])

    with st.expander("🩺 Symptoms"):
        for symptom in info["symptoms"]:
            st.markdown(f"• {symptom}")

    with st.expander("⚠ Risk Factors"):
        for risk in info["risk_factors"]:
            st.markdown(f"• {risk}")

    with st.expander("💊 General Treatment"):
        st.write(info["treatment"])

    return info