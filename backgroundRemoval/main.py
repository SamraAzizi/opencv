import cv2
import cvzone
from cvzone import SelfieSegmentation
import os
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
segmentor = SelfieSegmentation()
fpsReader = cvzone.FPS()

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (255,0,255), threshold = 0.8)
    


    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    fpsReader.update(img)

    
    cv2.imshow("Image", img)
<<<<<<< HEAD
    cv2.waitKey(1)
=======
    cv2.imshow("ImageOut", imgOut)
    cv2.waitKey(1)
>>>>>>> d940948eb0e2e24ed8fe158c11524de700bfa232
