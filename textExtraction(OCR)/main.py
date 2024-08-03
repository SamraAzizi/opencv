import cv2
from PIL import Image
import pytesseract
import os



my_config = r"--psm 6 --oem 3"
img = cv2.imread(r"C:\Users\CPCM\OneDrive\Desktop\opencv\textExtraction(OCR)\txt.jpg")

if img is None:
    raise FileNotFoundError("Image file not found. Please check the path.")

height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=my_config)

for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
