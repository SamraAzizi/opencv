import cv2

webcame = cv2.VideoCapture(0)

my_hands = mp.solutions.hans.Hands()
drwaing_utils = mp.solutions.drawing_utlis

while True:
    _, image = webcame.read()
    frame_width, frame_height = image.shape()

    
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drwaing_utils.draw_landmarks(image, hand)
            landmarks = hand.handmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img= image, center = (x, y), radius=8, color = (0,255, 255), thickness = 3)

                if id == 4:
                    cv2.circle(img= image, center = (x, y), radius=8, color = (0,0, 255), thickness = 3)


    cv2.imshow("Hand Volume Control Using Python", image)
    key = cv2.waitKey(10)

    if key == 27:
        break


webcame.release()
cv2.destroyAllWindows()