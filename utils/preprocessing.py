import numpy as np
from PIL import Image

from tensorflow.keras.applications.efficientnet import preprocess_input

IMG_SIZE = (224, 224)

def preprocess_image(uploaded_file):

    image = Image.open(uploaded_file).convert("RGB")

    image = image.resize(IMG_SIZE)

    image_array = np.array(image, dtype=np.float32)

    # Use the SAME preprocessing as training
    image_array = preprocess_input(image_array)

    image_array = np.expand_dims(image_array, axis=0)

    return image, image_array