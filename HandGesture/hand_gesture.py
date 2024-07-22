import cv2

webcame = cv2.VideoCapture(0)

my_hands = mp.solutions.hans.Hands()
drwaing_utils = mp.solutions.drawing_utlis

while True:
    _, image = webcame.read()
    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drwaing_utils.draw_landmarks(image, hand)
            landmarks = hand.handmark
            for id, _landmark in enumerate(landmarks):
                if id == 8:
                    cv2.circle(img= image, center = (x, y))


    cv2.imshow("Hand Volume Control Using Python", image)
    key = cv2.waitKey(10)

    if key == 27:
        break


webcame.release()
cv2.destroyAllWindows()