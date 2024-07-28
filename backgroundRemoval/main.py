import cv2
import cvzone
from cvzone.SelfieSegmentationModule import SelfieSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
