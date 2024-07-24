import cv2

cap = cv2.VideoCapture("highway.mp4")

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)