import cv2
from matplotlib import pyplot as plt
import imutils
import easyocr


img = cv2.imread('123.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)