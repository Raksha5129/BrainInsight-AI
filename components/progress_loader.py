import streamlit as st
import time


def show_progress():

    progress = st.progress(0)

    status = st.empty()

    for i in range(100):

        progress.progress(i + 1)

        if i < 30:
            status.info("Loading MRI...")

        elif i < 60:
            status.info("Analyzing Brain Structures...")

        elif i < 90:
            status.info("Running EfficientNetB0...")

        else:
            status.success("Prediction Complete!")

        time.sleep(0.01)

   ##st.balloons()