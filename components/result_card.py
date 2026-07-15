import streamlit as st

def show_result(prediction, confidence):

    st.markdown("---")

    st.markdown(
        """
        <h2 style='text-align:center;color:#2563EB;'>
        🧠 AI Diagnosis Result
        </h2>
        """,
        unsafe_allow_html=True
    )

    c1,c2,c3=st.columns(3)

    with c1:

        st.success("Prediction")

        st.markdown(
            f"""
            <h2 style='text-align:center'>
            {prediction}
            </h2>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.info("Confidence")

        st.markdown(
            f"""
            <h2 style='text-align:center'>
            {confidence:.2f}%
            </h2>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.warning("Risk Level")

        if confidence>95:

            level="🔴 High"

        elif confidence>80:

            level="🟠 Medium"

        else:

            level="🟢 Low"

        st.markdown(
            f"""
            <h2 style='text-align:center'>
            {level}
            </h2>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")