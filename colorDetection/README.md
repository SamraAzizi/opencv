# Color Detection using OpenCV
================================

## Overview
-----------

This code is a color detection program that uses OpenCV to detect and display different colors in real-time using a webcam. The program can detect four colors: yellow, red, green, and blue.

## How it Works
----------------

The program uses the following steps to detect colors:

* **Convert BGR to HSV**: The program converts the BGR (Blue, Green, Red) color format to HSV (Hue, Saturation, Value) format, which is more suitable for color detection.
* **Define Color Limits**: The program defines the lower and upper limits for each color in HSV format, with a range of 10 around the hue value.
* **Capture Video**: The program captures video from the default camera (index 0) using OpenCV.
* **Loop through Colors**: The program loops through each color and applies a mask to the video frame based on the HSV values.
* **Display Masks**: The program displays the mask for each color detection.

## Usage
-----

1. Run the program using Python (e.g., `python color_detection.py`).
2. The program will display four windows, each showing the detection of a different color (yellow, red, green, and blue).
3. Press 'q' to exit the program.

## Dependencies
--------------

* OpenCV (cv2)
* NumPy (np)

## Code Structure
-----------------

The code is organized into the following sections:

* **Importing Libraries**: Importing necessary libraries (OpenCV and NumPy).
* **Defining Color Limits Function**: Defining a function to get the HSV limits for a given BGR color.
* **Defining Colors**: Defining the BGR values for each color (yellow, red, green, and blue).
* **Capturing Video**: Capturing video from the default camera using OpenCV.
* **Color Detection Loop**: Looping through each color and applying the mask to the video frame.
* **Displaying Masks**: Displaying the mask for each color detection.
* **Exiting the Program**: Exiting the program when 'q' is pressed.