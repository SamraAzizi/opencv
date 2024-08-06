# Text Extraction (OCR) with OpenCV and Tesseract

This project demonstrates how to perform Optical Character Recognition (OCR) using OpenCV and Tesseract. The code loads an image, processes it with Tesseract to extract text, and then highlights the detected text on the image.






## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- Pillow (PIL)
- Tesseract-OCR
- pytesseract

## Installation

### Python Libraries

Install the required Python libraries using pip:

```sh
pip install opencv-python pillow pytesseract
```


## Tesseract-OCR

You also need to have Tesseract-OCR installed on your system. You can download it from the official [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).

Ensure that Tesseract-OCR is added to your system PATH.

## Usage

1. Place your image in the specified path. Update the `img = cv2.imread(r"C:\path\to\your\image.jpg")` line in the code to the correct path of your image file.

2. Run the script:

```sh
python script.py
```

## The script will:

- Load the image.
- Use Tesseract to detect text and its bounding boxes.
- Draw rectangles around the detected text with confidence levels above 80%.
- Display the processed image with detected text highlighted.
