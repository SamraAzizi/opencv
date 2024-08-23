import cv2
import numpy as np


cap = cv2.VideoCapture(0)

imgTarget = cv2.imread("cards.jpg")
myVideo = cv2.VideoCapture()

success , imgVideo = myVid.read()


hT, wT, cT = imgTarget.shape
imgVideo = cv2.resize(imgVideo, (wT, hT))

orb = cv2.ORB_create(nfeatures = 1000)

kp1, des1 = orb.detectAndCompute(imgTarget, None)

imgTarget = cv2.drawKeypoints(imgTarget, kp1, None)

while True:
        
        
        success, imgWebcam = cap.read()
        kp2, des2 = orb.detectAndCompute(imgWebcam, None)
        imgWebcam = cv2.drawKeypoints(imgWebcam, kp2, None)
        




        cv2.imshow("ImageTarget", imgTarget)
        cv2.imshow("myVideo", imgVideo)
        cv2.imshow("imgWebcam", imgWebcam)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                    break