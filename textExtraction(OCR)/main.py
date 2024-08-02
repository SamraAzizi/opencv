import cv2
from PIL import Image
import pytesseract
import os


'''
# Use the absolute path to the image file
image_path = r"C:\Users\CPCM\OneDrive\Desktop\opencv\textExtraction(OCR)\text.jpg"

# Check if the file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"No such file: '{image_path}'")

# Open the image file
image = Image.open(image_path)

# Specify Tesseract configuration
my_config = r"--psm 6 --oem 3"

# Perform OCR on the image
text = pytesseract.image_to_string(image, config=my_config)

# Print the extracted text
print(text)


'''


##########################################

my_config = r"--psm 6 --oem 3"
img = cv2.imread("txt.jpg")

height, width, _ = img.shape()