import numpy as np
import requests
from keras.models import load_model
from PIL import Image


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


def predict_img(url):
    response = requests.get(url, stream=True)
    img = Image.open(response.raw)
    img = img.resize((32, 32))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    model = load_model("cnn_86.keras")
    prediction = model.predict(img)
    index = np.argmax(prediction[0])
    return class_names[index]


if __name__ == "__main__":
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsa3ISspmdRq4nDC9M6pfoNh1TvukFHBzGuA&usqp=CAU"
    result = predict_img(url)
    print(result)
