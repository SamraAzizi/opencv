import cv2

face_cascade = cv2.CascadeClassrifier('harrcascade_frontalface_default.xml')


webcam = cv2.VideoCapture(0)

while True:
    _, img = webcam.read()
    cv2.imshow("FACE DETECTION", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5)
    key = cv2.waitKey(10)
    if key == 27:
        break


webcam.release()
cv2.destroyAllWindows()
