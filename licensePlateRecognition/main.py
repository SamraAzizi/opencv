import cv2
from matplotlib import pyplot as plt
import imutils
import easyocr


img = cv2.imread('123.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))


bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
