import streamlit as st

from utils.disease_info import DISEASE_INFO
from components.footer import show_footer
st.set_page_config(
    page_title="Disease Library",
    page_icon="📚",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.image("assets/logo_with_text.png", width=400)

st.title("📚 Brain Disease Library")

st.write(
    "Learn about the neurological diseases supported by BrainInsight AI."
)

st.divider()

disease = st.selectbox(
    "Select a Disease",
    list(DISEASE_INFO.keys())
)

info = DISEASE_INFO[disease]
st.divider()

st.subheader("📊 Quick Facts")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Disease", disease)

with c2:
    st.metric("Category", "Neurological")

with c3:
    st.metric("AI Detection", "Supported")
show_footer()