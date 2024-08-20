   


import cv2
import time
import main as pm

cap = cv2.VideoCapture(r"C:\Users\CPCM\OneDrive\Desktop\opencv\poseEstimation\123.mp4")

prevTime = 0
detector = pm.PoseDetector()

while True:

    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if lmList:
       
cap.release()
cv2.destroyAllWindows()


if __name__ == "__main__":
    main()