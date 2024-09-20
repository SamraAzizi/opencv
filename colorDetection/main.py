import numpy as np
import cv2
from util import get_limits
from PIL import Image  # Fixed import, should be "Image" from PIL, not "pillow"

yellow = [0, 255, 255]
cap = cv2.VideoCapture(2)

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
    mask = cv2.inRange(hsvImage, np.array(lowerLimit), np.array(upperLimit))

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
