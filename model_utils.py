# Dummy file for model_utils.py
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

MODEL_PATH = "models/pollen_model.h5"

def load_model_and_predict(image_file):
    model = load_model(MODEL_PATH)
    img = image.load_img(image_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    return prediction.tolist()
