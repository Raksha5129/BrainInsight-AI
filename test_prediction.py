from PIL import Image
from predict import predict

image = Image.open("sample_images/test.jpg")

disease, confidence, probs = predict(image)

print("Prediction :", disease)
print("Confidence :", confidence)

print("\nAll Probabilities")

for k, v in probs.items():
    print(k, ":", round(v,2), "%")