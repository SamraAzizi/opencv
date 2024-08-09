import cv2

import imutils
import winsound
import threading


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width = 500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)