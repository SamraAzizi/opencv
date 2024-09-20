import numpy as np
import cv2
from util import get_limits


yellow = [0,255,255]
cap = cv2.VideoCapture(2)

while True:
    ret, frame, = cap.read()

    cv2.cvtColor(frame , cv2.COLORBGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)


    mask = cv2.inRange(hsvImage,lowerLimit, upperLimit )



    cv2.imshow('frame', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release
cv2.destroyAllWindows()