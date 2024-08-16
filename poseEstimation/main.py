import opencv
import mediapipe as mp
import time


cap = cv2.VideoCapture("")

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)

    currentTime = 
    cv2.waitKey(1)