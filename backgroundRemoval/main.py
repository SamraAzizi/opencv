import cv2
import cvzone
import mediapipe as mp
import os
import numpy as np

cap = cv2.VideoCapture(0)

imgBg = cv2.imread("Images/2.jpg")
segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection = 1)
while cap.isOpened():
    ret, frame = cap.read()
    height, width, channel = frame.shape
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = segmentation.process(RGB)
    mask = results.segmentationi_mask
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgBg, threshold = 0.8)
    


    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    

    cv2.imshow("Image", img)
    cv2.waitKey(1)