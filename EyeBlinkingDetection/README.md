# Eye Blink Detection using OpenCV and Dlib

## Overview

This project uses OpenCV and Dlib libraries to detect eye blinks in real-time video capture. The code calculates the blinking ratio of the eyes and displays "BLINKING" on the screen when the ratio exceeds a certain threshold.

## Dependencies

* OpenCV (cv2)
* Dlib
* NumPy (np)
* Math library (for hypot function)
aces, calculates blinking ratio, and displays the result.

### Variables

* `cap`: video capture object.
* `detector`: Dlib's face detector.
* `predictor`: Dlib's facial landmark predictor.
* `font`: font for displaying text.
* `eye_points`: list of facial landmarks for the eye.
* `facial_landmarks`: facial landmarks for the face.
* `frame`: current video frame.
* `blinking_ratio`: average blinking ratio of both eyes.

## Threshold Adjustment

The threshold value (5.7) for blinking ratio detection may need to be adjusted based on individual variations in eye shape and size. You can adjust this value by analyzing the printed blinking ratio values during script execution.