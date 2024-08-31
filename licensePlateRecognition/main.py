import cv2
from matplotlib import pyplot as plt
import imutils
import easyocr
import numpy as np

# Load the image
img = cv2.imread('123.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

# Apply bilateral filtering to the grayscale image
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edge = cv2.Canny(bfilter, 30, 200)
plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))

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

# Create a mask for the license plate
mask = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask, [location], 0, 255, -1)

# Apply the mask to the original image
new_image = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))

# Get the bounding box of the license plate
(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]

plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

# Use EasyOCR to read the text from the license plate
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)

# Get the text from the result
text = result[0][-2]

# Draw the text on the original image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text=text, org=(location[0][0][0], location[1][0][1]+60), fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# Draw a rectangle around the license plate
cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0, 255, 0), 3)

# Display the final image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))