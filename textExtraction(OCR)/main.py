import cv2

my_config = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("txt.jpg"))