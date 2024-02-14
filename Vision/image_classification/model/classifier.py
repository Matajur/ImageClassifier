import numpy as np
import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img


class_names = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck",
]

def predict_img(file_path):
    
    model_path = os.path.join(os.path.dirname(__file__), "cnn_model.keras")
    model = load_model(model_path)
    
    img = load_img(file_path, target_size=(32, 32))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    return predicted_class


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "plane.jpg")
    result = predict_img(file_path)
    print(result)
