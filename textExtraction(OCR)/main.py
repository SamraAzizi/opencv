import cv2
from PIL import Image
import pytesseract
import os
from pytesseract import Output 



my_config = r"--psm 6 --oem 3"
img = cv2.imread(r"C:\Users\CPCM\OneDrive\Desktop\opencv\textExtraction(OCR)\logo.jpg")

#if img is None:
 #   raise FileNotFoundError("Image file not found. Please check the path.")

#height, width, _ = img.shape

#boxes = pytesseract.image_to_boxes(img, config=my_config)

#for box in boxes.splitlines():
   # box = box.split(" ")
   # img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)



data = pytesseract.image_to_data(img, config=my_config, output_type=Output.DICT )

amount_of_boxes = len(data['text'])

for i in range(amount_of_boxes):
    if float(data['conf'][i]) > 80:
        (x, y, width, height) = (data['left'][i], data['top'][i],  data['width'][i], data['height'][i])

        img = cv2.rectangle(img, (x,y), (x+width, y + height), (0,255,0), 2)
        img = cv2.putText(img, data['text'][i], (x,y+height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0), 2,cv2.LINE_AA)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
