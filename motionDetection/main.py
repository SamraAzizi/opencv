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
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

def beep_alarm():
    global alarm

    for _ in range(5):
        if not alarm_mode:
            break

        print("ALARM")
        winsound.Beep(2500, 1000)

    alarm = False

while True:

    _, frame = cap.read()
    frame = imutils.resize(frame, width = 500)
    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5,5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.treshold(difference, 25, 255, cv2.THRESHOLD_BINARY)[1]
