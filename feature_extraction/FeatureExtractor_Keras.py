from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input, Flatten, Dense
from keras.models import Model

import cv2
import numpy as np
import scipy.io

def feature_extraction(image_path):
    model = VGG16(weights='imagenet', include_top=True)

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)


    featextractor_model = Model(input=model.input, outputs=model.get_layer('fc2').output)
    features = featextractor_model.predict(x)
    # print features
    return features

def feature_extraction_VGG19(image_path):
    base_model = VGG19(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    block4_pool_features = model.predict(x)
    return block4_pool_features

if __name__ == '__main__':

    model = VGG16(weights='imagenet', include_top=True)

    img_path = 'image/dog.jpg'

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)


    featextractor_model = Model(input=model.input, outputs=model.get_layer('fc2').output)
    features = featextractor_model.predict(x)
    print features
    np.save('feat_test.npy', features)

