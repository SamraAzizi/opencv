# Hand Gesture Volume Control

This project uses a webcam to control the system volume based on hand gestures. The project utilizes OpenCV for image processing, MediaPipe for hand tracking, and PyAutoGUI for controlling the volume.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Notes](#notes)
- [Troubleshooting](#troubleshooting)


## Prerequisites

Ensure you have the following libraries installed:

- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

You can install the necessary dependencies using pip:

```bash
pip install opencv-python mediapipe pyautogui





## Features

- **Hand Tracking**: Uses MediaPipe to track hand landmarks.
- **Volume Control**: Uses the distance between the thumb and index finger to control the system volume. If the distance is greater than a certain threshold, the volume is increased. If it is less, the volume is decreased.

## Notes

- Ensure your webcam is connected and working.
- The script uses the default webcam (index 0). If you have multiple webcams, you may need to change the index in the line `webcam = cv2.VideoCapture(0)`.
- Good lighting conditions help improve hand landmark detection accuracy.
- Make sure your hand is visible to the webcam and is not moving too quickly for accurate detection.

## Troubleshooting

- **Import Errors**: If the script fails to import the libraries, ensure they are installed correctly using pip:
  ```bash
  pip install opencv-python mediapipe pyautogui
