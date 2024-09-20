import numpy as np
import cv2
from util import get_limits

cap = cv2.VideoCapture(2)

while True:
    ret, frame, = cap.read()

    cv2.cvtColor(frame , cv2.COLORBGR2HSV)


    mask = cv2.inRange(hsvImage, )



    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release
cv2.destroyAllWindows()