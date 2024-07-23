
# Hand Gesture Volume Control

This project uses a webcam to control the system volume based on hand gestures. The project utilizes OpenCV for image processing, MediaPipe for hand tracking, and PyAutoGUI for controlling the volume.
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

You can install these dependencies using pip:

```bash
pip install opencv-python mediapipe pyautogui


## Features

- **Hand Tracking**: Utilizes MediaPipe to track hand landmarks.
- **Volume Control**: Controls the system volume based on the distance between the thumb and index finger. If the distance exceeds a specific threshold, the volume increases; otherwise, the volume decreases.

## Notes

- Ensure your webcam is connected and functioning properly.
- The script uses the default webcam (index 0). If you have multiple webcams, you may need to change the index in the line `webcam = cv2.VideoCapture(0)`.
- Good lighting conditions will improve the accuracy of hand landmark detection.
- Place your hand clearly in front of the webcam and avoid rapid movements for better detection.

## Troubleshooting

- **Import Errors**: If the script fails to import the required libraries, ensure they are installed correctly using pip:
  ```bash
  pip install opencv-python mediapipe pyautogui
