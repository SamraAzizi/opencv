import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]]) # here insert the bgr values which you want to convert
    hsvC = cv2