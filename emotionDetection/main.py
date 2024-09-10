from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np


face_classifier = cv2.CascadeClassifier(r'C:\Users\CPCM\OneDrive\Desktop\opencv\emotionDetection\haarcascade_frontalface_default.xml')

classifier = load_model(r'C:\Users\CPCM\OneDrive\Desktop\opencv\emotionDetection\model.h5')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)