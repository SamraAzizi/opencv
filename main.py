import cv2

face_cascade = cv2.CascadeClassrifier('harrcascade_frontalface_default.xml')


webcam = cv2.VideoCapture(0)