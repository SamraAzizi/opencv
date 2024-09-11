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
    faces = face_classifier.detectMultiScale(gray)


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation= cv2.INTER_AREA)


        if np.sum([roi_gray])!= 0:
            roi = roi_gray
                  

    