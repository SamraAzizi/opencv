   


import cv2
import time
import main as pm

cap = cv2.VideoCapture(r"C:\Users\CPCM\OneDrive\Desktop\opencv\poseEstimation\123.mp4")

prevTime = 0
detector = pm.PoseDetector()

while True:

    success, img = cap.read()


if __name__ == "__main__":
    main()