# Eye Blink Detection using OpenCV and Dlib

## Overview

This project uses OpenCV and Dlib libraries to detect eye blinks in real-time video capture. The code calculates the blinking ratio of the eyes and displays "BLINKING" on the screen when the ratio exceeds a certain threshold.

## Dependencies

1. Install the required dependencies.
2. Run the script using Python.
3. The script will capture video from the default camera (index 0).
4. The script will display the video feed with annotations.
5. When the blinking ratio exceeds the threshold (5.7 in this case), the script will display "BLINKING" on the screen.
6. Press the 'ESC' key to exit the script.

## Code Explanation

### Functions

* `midpoint(p1, p2)`: calculates the midpoint between two points.
* `get_blinking_ratio(eye_points, facial_landmarks, frame)`: calculates the blinking ratio of an eye.
* `main loop`: captures video, detects faces, calculates blinking ratio, and displays the result.

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