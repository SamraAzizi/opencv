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
    imgOut = segmentor.removeBG(img, (255,0,255))

    
