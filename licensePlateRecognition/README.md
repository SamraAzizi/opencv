# License Plate Recognition using OpenCV and Tesseract-OCR

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Code Explanation](#code-explanation)

## Introduction
This project demonstrates a license plate recognition application using OpenCV and Tesseract-OCR. It uses image processing techniques to detect and recognize license plates in images.

## Requirements
* OpenCV 4.x
* Tesseract-OCR 4.x
* Pytesseract 0.3.x
* Imutils 0.5.x
* Matplotlib 3.x
* NumPy 1.x

## Usage
1. Clone this repository and navigate to the project directory.
2. Install the required dependencies by running `pip install opencv-python pytesseract imutils matplotlib numpy`.
3. Download the Tesseract-OCR engine from the official GitHub repository: https://github.com/tesseract-ocr/tesseract
4. Add the path to the Tesseract-OCR engine to your system's PATH environment variable.
5. Replace the image path in the code with the path to your own image.
6. Run the code by executing `python license_plate_recognition.py`.
7. The application will display several windows:
	* "Grayscale Image": shows the grayscale image.
	* "Edge Detection": shows the edges detected in the image.
	* "Masked Image": shows the masked image with the detected license plate.
	* "Cropped License Plate": shows the cropped license plate.
	* "Final Image with Detected Text": shows the final image with the detected text.
8. Press 'q' to exit the application.

## Code Explanation
The code uses the following steps to achieve license plate recognition:

1. Load the image and convert it to grayscale.
2. Apply bilateral filtering to the grayscale image.
3. Detect edges in the filtered image using Canny edge detection.
4. Find contours in the edge map and approximate the contour with a polygon.
5. Create a mask for the license plate and apply it to the original image.
6. Get the bounding box of the license plate and crop it.
7. Use Tesseract-OCR to read the text from the cropped license plate.
8. Draw the text on the original image.
9. Display the images.

### Importing Libraries
```python
import cv2
from matplotlib import pyplot as plt
import imutils
import pytesseract
import numpy as np