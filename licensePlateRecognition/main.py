import cv2
from matplotlib import pyplot as plt
import imutils
import pytesseract
import numpy as np

# Load the image
img = cv2.imread('C:/Users/CPCM/OneDrive/Desktop/opencv/licensePlateRecognition/123.jpg')

# Check if the image is loaded successfully
if img is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
plt.im
plt.show()

# Find the contours in the edge map
keyPoints = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keyPoints)
contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)[:10]

location = None
for contour in contours:
    # Approximate the contour with a polygon
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

# Ensure a location was found
if location is None:
    print("Error: No license plate detected.")
    exit()

# Create a mask for the license plate
mask = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask, [location], 0, 255, -1)

# Apply the mask to the original image
new_image = cv2.bitwise_and(img, img, mask=mask)

# Display the masked image
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.title('Masked Image')
plt.axis('off')
plt.show()

# Get the bounding box of the license plate
(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]

# Display the cropped license plate
plt.imshow(cropped_image, cmap='gray')
plt.title('Cropped License Plate')
plt.axis('off')
plt.show()

# Use Tesseract-OCR to read the text from the license plate
text = pytesseract.image_to_string(cropped_image, lang='eng', config='--psm 11')
print(f"Detected text: {text}")

# Draw the text on the original image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text=text.strip(), org=(location[0][0][0], location[0][0][1] - 10), 
            fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# Draw a rectangle around the license plate
cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0, 255, 0), 3)

# Display the final image with detected text
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Final Image with Detected Text')
plt.axis('off')
plt.show()
