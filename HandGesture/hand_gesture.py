import cv2

webcame = cv2.VideoCapture(0)

my_hands = mp.solutions.hans.Hands()
drwaing_utils = mp.solutions.drawing_utlis

while True:
    _, image = webcame.read()
    cv2.imshow("Hand Volume Control Using Python", image)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    key = cv2.waitKey(10)

    if key == 27:
        break


webcame.release()
cv2.destroyAllWindows()