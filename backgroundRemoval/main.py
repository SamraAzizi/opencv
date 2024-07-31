import cv2
import cvzone
import mediapipe as mp
import os
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection = 1)
fpsReader = cvzone.FPS()

imgBg = cv2.imread("Images/2.jpg")

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgBg, threshold = 0.8)
    


    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0,0,255))

    cv2.imshow("Image", img)
    cv2.waitKey(1)