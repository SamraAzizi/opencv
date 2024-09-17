import cv2
import numpy as np
import dlib
from math import hypot

# Initialize video capture
cap = cv2.VideoCapture(0)

# Load Dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\CPCM\OneDrive\Desktop\opencv\eyeDetection\shape_predictor_68_face_landmarks.dat")

# Function to calculate midpoint between two points
def midpoint(p1, p2):
    return (int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2))

# Set font for displaying text
font = cv2.FONT_HERSHEY_PLAIN

# Function to calculate the blinking ratio
def get_blinking_ratio(eye_points, facial_landmarks, frame):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)

    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    # Draw horizontal and vertical lines on the eye (for debugging/visualization)
    horizontal_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    vertical_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    # Calculate lengths of the horizontal and vertical lines
    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    # Calculate the ratio
    ratio = hor_line_length / ver_line_length

    # Print the ratio for debugging purposes
    #print(f"Blinking Ratio: {ratio}")

    return ratio

# Main loop for video capture
while True:
    _, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get coordinates of the face
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()

        # Get facial landmarks
        landmarks = predictor(gray, face)

        # Calculate blinking ratio for both eyes
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks, frame)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks, frame)

        # Average blinking ratio
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        # If blinking ratio exceeds threshold, display "BLINKING"
        # Adjust the threshold based on the printed ratio values
        if blinking_ratio > 5.7:
            cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0), 3)

    # Display the frame with annotations
    cv2.imshow("Frame", frame)

    # Exit loop on pressing 'ESC' key
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
