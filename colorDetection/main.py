import numpy as np
import cv2

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

# Define colors in BGR format
yellow = [0, 255, 255]  # Yellow
red = [0, 0, 255]       # Red
green = [0, 255, 0]     # Green
blue = [255, 0, 0]      # Blue

colors = {'Yellow': yellow, 'Red': red, 'Green': green, 'Blue': blue}

cap = cv2.VideoCapture(0)  # Use 0 or another index to select the correct camera

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame from BGR to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Loop through each color and apply the mask
    for color_name, bgr_color in colors.items():
        # Get the color limits (lower and upper bounds) for the current color
        lowerLimit, upperLimit = get_limits(color=bgr_color)

        # Create a mask for the color detection based on HSV values
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        # Display the mask for the current color
        cv2.imshow(f'{color_name} Detection', mask)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
