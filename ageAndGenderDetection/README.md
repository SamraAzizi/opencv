# Age and Gender Detection using OpenCV
=====================================

## Overview
-----------

This code uses OpenCV to detect faces in an image and predict the age and gender of each detected face. It utilizes pre-trained models for face detection, age prediction, and gender prediction.

## Requirements
------------

* OpenCV library
* Pre-trained models for face detection, age prediction, and gender prediction (provided in the `models` directory)

## Usage
-----

1. Place the image file to be processed in the same directory as the script.
2. Update the `image_path` variable to point to the image file.
3. Run the script using Python (e.g., `python script.py`).
4. The script will display the output image with detected faces and predicted age and gender.

## Code Explanation
-----------------

### Importing Libraries and Setting Up Models

The script starts by importing the necessary libraries, including OpenCV. It then sets up the working directory to the `models` directory, where the pre-trained models are stored.

### Loading Models and Image

The script loads the pre-trained models for face detection, age prediction, and gender prediction. It also loads the input image and checks if it exists.

### Face Detection and Prediction

The script performs face detection using the OpenCV `dnn` module and the pre-trained face detection model. It then iterates through the detected faces, extracts the face region, and predicts the age and gender using the pre-trained age and gender prediction models.

### Displaying Results

The script displays the output image with detected faces and predicted age and gender using OpenCV's `imshow` function.

## Note
-----

This script assumes that the pre-trained models are stored in the `models` directory and that the input image is in the same directory as the script. You may need to adjust the file paths accordingly.