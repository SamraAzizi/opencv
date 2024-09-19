import numpy as np
import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, frame, = cap.read()

    cv2.cvtColor(frame , cv2.COLORBGR2HSV)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release
cv2.destroyAllWindows()