import cv2

webcame = cv2.VideoCapture(0)

while True:
    _, image = webcame.read()
    cv2.imshow("Hand Volume Control Using Python", image)
    key = cv2.waitKey(10)

    if key == 27:
        break


webcame.release()
cv2.destroyAllWindows()