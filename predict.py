import numpy as np
from PIL import Image
import tensorflow as tf

# Load trained model
MODEL_PATH = "model/BrainInsight_Final.keras"

model = tf.keras.models.load_model(MODEL_PATH)

# Class names
CLASS_NAMES = [
    "Alzheimer",
    "Multiple Sclerosis",
    "Normal",
    "Stroke",
    "Tumor"
]


def preprocess_image(image):

    image = image.convert("RGB")
    image = image.resize((224, 224))

    image = np.array(image).astype(np.float32)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image


def predict(image):

    img = preprocess_image(image)

    prediction = model.predict(img, verbose=0)

    predicted_class = CLASS_NAMES[np.argmax(prediction)]

    confidence = float(np.max(prediction) * 100)

    probabilities = {
        CLASS_NAMES[i]: float(prediction[0][i] * 100)
        for i in range(len(CLASS_NAMES))
    }

    return predicted_class, confidence, probabilities