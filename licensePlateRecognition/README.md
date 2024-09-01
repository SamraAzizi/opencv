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
6. Run the code by executing `main.py`.
7. The application will display several windows:
	* "Grayscale Image": shows the grayscale image.
	* "Edge Detection": shows the edges detected in the image.
	* "Masked Image": shows the masked image with the detected license plate.
	* "Cropped License Plate": shows the cropped license plate.
	* "Final Image with Detected Text": shows the final image with the detected text.
