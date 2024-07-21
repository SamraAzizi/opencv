import cv2

webcame = cv2.VideoCapture(0)

while True:
    _, image = webcame.read()
    cv2.imshow("Hand Volume Control Using Python", image)
    cv2.waitKey(10)