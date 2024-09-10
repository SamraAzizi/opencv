from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np


face_classifier = cv2.CascadeClassifier(r'C:\Users\CPCM\OneDrive\Desktop\opencv\emotionDetection\haarcascade_frontalface_default.xml')

