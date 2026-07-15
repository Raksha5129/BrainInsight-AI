import streamlit as st


def show_recommendation(result):

    st.subheader("📌 Medical Recommendation")

    disease = result["prediction"]

    if disease == "Tumor":

        st.error("""
### 🧠 Brain Tumor

• Consult a neurologist or neurosurgeon.

• MRI findings should be reviewed by a radiologist.

• Additional clinical evaluation may be required.
""")

    elif disease == "Stroke":

        st.error("""
### 🩸 Stroke

• Immediate medical attention is recommended.

• Time-sensitive treatment is critical.

• Consult a neurologist immediately.
""")

    elif disease == "Alzheimer":

        st.warning("""
### 🧠 Alzheimer's Disease

• Cognitive assessment is recommended.

• Consult a neurologist.

• Follow-up evaluation may be required.
""")

    elif disease == "Multiple Sclerosis":

        st.warning("""
### 🧬 Multiple Sclerosis

• Neurological examination is advised.

• MRI findings should be correlated clinically.
""")

    else:

        st.success("""
### ✅ Normal Brain MRI

No abnormal brain disease detected.

If symptoms persist, consult a healthcare professional.
""")