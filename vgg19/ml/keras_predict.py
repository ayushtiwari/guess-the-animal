import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import img_to_array


def get_model():
    model = load_model('vgg19/ml/vgg16_fine_tuned.h5')
    return model


def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)/255.0
    image = np.expand_dims(image, axis=0)
    return image


def predict(image):

    image = preprocess_image(image, (224, 224))
    model = get_model()
    pred = model.predict(image)

    if pred.argmax(axis=1)[0] == 0:
        return {'animal': 'Cat', 'prob': pred[0][0]*100}
    else:
        return {'animal': 'Dog', 'prob': pred[0][1]*100}


