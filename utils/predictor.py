 
import streamlit as st
import tensorflow as tf
import numpy as np

from utils.preprocessing import preprocess_image
# Load model only once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model/BrainInsight_Final.keras")

# Load the model only once and reuse it
model = load_model()

CLASSES = [
    "Alzheimer",
    "Multiple Sclerosis",
    "Normal",
    "Stroke",
    "Tumor"
]


def predict(uploaded_file):

    # Preprocess image
    original_image, img = preprocess_image(uploaded_file)

    # Prediction
    prediction = model.predict(img, verbose=0)[0]
    print("Raw Prediction:", prediction)

    index = np.argmax(prediction)

    disease = CLASSES[index]

    confidence = float(prediction[index] * 100)

    probabilities = {
        CLASSES[i]: float(prediction[i] * 100)
        for i in range(len(CLASSES))
    }

    return {
    "image": original_image,
    "prediction": disease,
    "confidence": confidence,
    "probabilities": probabilities
}