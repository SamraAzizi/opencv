import cv2
import PIL.Image
import pytesseract

my_config = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("txt.jpg"), config=my_config)

print(text)