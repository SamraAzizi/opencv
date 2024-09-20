import numpy as np
import cv2
from PIL import Image  # Fixed import, should be "Image" from PIL, not "pillow"

# Define the function to get HSV limits for a given BGR color
def get_limits(color):
    # Convert BGR to HSV
    bgr_color = np.uint8([[color]])  # Convert color to a format usable by OpenCV
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)

    hue = hsv_color[0][0][0]
    
    # Define limits with some range around the hue
    lower_limit = np.array([hue - 10, 100, 100])
    upper_limit = np.array([hue + 10, 255, 255])
    
    return lower_limit, upper_limit

yellow = [0, 255, 255]  # BGR format for yellow
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame from BGR to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the color limits (lower and upper bounds) for yellow
    lowerLimit, upperLimit = get_limits(color=yellow)

    # Create a mask for the color detection based on HSV values
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Convert mask to an image using PIL
    mask_image = Image.fromarray(mask)

    # Display the mask
    cv2.imshow('frame', mask)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
