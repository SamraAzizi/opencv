import cv2
import mediapipe as mp
import pyautogui


x1 = y1 = x2 = y2 = 0

# Initialize the webcam
webcam = cv2.VideoCapture(0)

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

while True:
    ret, image = webcam.read()
    if not ret:
        break
    image = cv2.flip(image, 1)

    frame_height, frame_width, _ = image.shape

    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    output = hands.process(rgb_image)
    hands_landmarks = output.multi_hand_landmarks

    if hands_landmarks:
        for hand_landmarks in hands_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for id, landmark in enumerate(hand_landmarks.landmark):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(image, (x, y), 8, (0, 255, 255), 3)

                    x1 = x
                    y1 = y
                
                if id == 4:
                    cv2.circle(image, (x, y), 8, (0, 0, 255), 3)
                    x2 = x
                    y2 = y

        distance = ((x2-x1) **2 + (y2-y1) ** 2)**(0.5) // 4

        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0),5)

        if distance > 50 :
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")
    # Display the image
    cv2.imshow("Hand Volume Control Using Python", image)

    # Bres()
