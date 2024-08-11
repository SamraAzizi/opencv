# Motion Detection Alarm System

This project is a simple motion detection alarm system using OpenCV and Python. It captures video from the webcam, processes the frames to detect motion, and triggers an alarm sound if significant motion is detected.

## Features

- **Motion Detection**: Detects motion by comparing the current frame with the previous frame.
- **Alarm Mode**: Can be toggled on/off using the 's' key.
- **Alarm Trigger**: If motion is detected consistently, an audible alarm is triggered.
- **User Control**: The program can be exited by pressing the 'q' key.

## Requirements

- Python 3.x
- OpenCV
- imutils
- winsound (Windows-only)
- threading (built-in)

## Installation

1. Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

2. Install the required Python packages using pip:
   ```bash
   pip install opencv-python imutils
