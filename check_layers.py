from tensorflow.keras.models import load_model

model = load_model("model/BrainInsight_Final.keras")

base_model = model.get_layer("efficientnetb0")

print("Total layers:", len(base_model.layers))

print("\nLast 20 layers:\n")

for layer in base_model.layers[-20:]:
    print(layer.name)