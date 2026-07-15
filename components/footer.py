import streamlit as st

def show_footer():

    st.divider()

    st.markdown(
        """
<div style="text-align:center;color:gray;padding:15px;">

🧠 <b>BrainInsight AI</b><br>

Deep Learning Based Multi-Class Brain Disease Detection<br><br>

TensorFlow • Streamlit • EfficientNetB0

</div>
""",
        unsafe_allow_html=True
    )