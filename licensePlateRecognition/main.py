import cv2
from matplotlib import pyplot as plt
import imutils
import easyocr
import numpy as np


img = cv2.imread('123.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))


bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edge = cv2.Canny(bfilter, 30, 200)
plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))


keyPoints = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APROX_SIMPLE)
contours = imutils.grab_contours(keyPoints)
contours = sorted(contours, key=cv2.contourArea, reverse= True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyOP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break


mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255,-1)
new_image = cv2.bitwise_and(img, img, mask = mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))


(x,y) = np.where(mask == 255)
(x1,y1) = (np.min(x), np.min(y))