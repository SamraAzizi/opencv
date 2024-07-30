import cv2
import cvzone
from cvzone import SelfieSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
segmentor = SelfieSegmentation()

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (255,0,255), threshold = 0.8)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)

    cv2.imshow("Image", img)
    cv2.imshow("ImageOut", imgOut)
    cv2.waitKey(1)