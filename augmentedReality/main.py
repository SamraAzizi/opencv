import cv2
import numpy as np


cap = cv2.VideoCapture(0)

imgTarget = cv2.imread("cards.jpg")
myVideo = cv2.VideoCapture()

success , imgVideo = myVid.read()


cv2.imshow("ImageTarget", imgTarget)
cv2.imshow("ImgTarget", imgVideo)

if cv2.waitKey(1) & 0xFF == ord('q'):
            break