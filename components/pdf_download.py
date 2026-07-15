import streamlit as st
from utils.report import generate_report

def show_pdf_download(result, info):

    st.subheader("📄 AI Medical Report")

    generate_report(
        result,
        info,
        "BrainInsight_Report.pdf"
    )

    with open("BrainInsight_Report.pdf", "rb") as pdf:

        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf.read(),
            file_name="BrainInsight_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )