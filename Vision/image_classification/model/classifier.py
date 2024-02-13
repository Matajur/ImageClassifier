import numpy as np
from keras.models import load_model
from PIL import Image
import os

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
    # Встановлюємо шлях до моделі відносно поточного файлу
    model_path = os.path.join(os.path.dirname(__file__), "cnn_86.keras")
    # Завантажуємо модель
    model = load_model(model_path)
    
    # Відкриваємо зображення, перетворюємо його і готуємо для прогнозування
    img = Image.open(file_path)
    img = img.resize((32, 32))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    
    # Робимо прогноз
    prediction = model.predict(img)
    index = np.argmax(prediction[0])
    
    # Повертаємо назву класу з найвищою ймовірністю
    return class_names[index]
