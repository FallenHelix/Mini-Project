import cv2
import time
import os, numpy as np
from PIL import Image
from threading import Thread
import face_recognition



def load_image_encoding():
    path = 'Training_images'
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]

    ids = []
    image_encodings = []
    for image in image_paths:
        print(os.path.split(image))
        image_id= os.path.split(image)[-1].split('.')[0]
        ids.append(image_id)
        path_image = face_recognition.load_image_file(image)
        image_encoding = face_recognition.face_encodings(path_image)[0]
        image_encodings.append(image_encoding)

    return image_encodings , ids

x,y = load_image_encoding()
print(y)
