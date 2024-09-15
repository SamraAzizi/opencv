import cv2
import numpy as np
import dlib
from math import hypot

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\CPCM\OneDrive\Desktop\opencv\eyeDetection\shape_predictor_68_face_landmarks.dat")

def midpoint(p1, p2):
    return (int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2))

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
       # cv2.rectangle(frame, (x,y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        left_point = (landmarks.part(36).x, landmarks.part(36).y)
        right_point = (landmarks.part(39).x, landmarks.part(39).y)

        center_top = midpoint(landmarks.part(37), landmarks.part(38))
        center_bottom = midpoint(landmarks.part(41), landmarks.part(40))

        horizontal_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
        ver_line = cv2.line(frame,center_top, center_bottom, (0,255, 0) ,2)


        hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
        ver_line_lenght = hypot((center_top[0] - center_bottom[0]), center_top[1] - center_bottom[1])

        
        

       # x = landmarks.part(36).x
       # y = landmarks.part(36).y
       # cv2.circle(frame, (x,y), 3, (0,0,255), 2)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()