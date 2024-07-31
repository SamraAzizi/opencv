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
    mask = results.segmentation_mask

    rsm = np.stack((mask, )*3, axis = -1)

    condition = rsm> 0.6
    condition = np.reshape(condition, (height, width, 3))

    background = cv2.resize(background, (width, height))

    output = np.where(condition, frame, background)

    cv2.imshow("output", output)

    k = cv2.waitKey(30) & 0xFF
    if k == (27):
        break


cap.release()
cap.destroyAllWindows()
