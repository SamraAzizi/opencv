import cv2

face_cascade = cv2.CascadeClassrifier('harrcascade_frontalface_default.xml')


webcam = cv2.VideoCapture(0)

while True:
    _, img = webcam.read()
    cv2.imshow("FACE DETECTION", img)
    key = cv2.waitKey(0)
    if key == 27:
        break
