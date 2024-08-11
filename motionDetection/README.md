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


How to Use
----------

1. Clone this repository or copy the code to your local machine.

2. Run the Python script:
   python motion_detection_alarm.py

3. The webcam will start capturing video. You will see the video feed in a window.

4. Toggle Alarm Mode: Press the 's' key to start or stop the alarm mode.

   - When alarm mode is on, the program wi
Frame Capturing:

- The code captures video frames using cv2.VideoCapture.
- It processes the frames by resizing, converting to grayscale, and applying Gaussian blur.

Motion Detection:

- The difference between the current and the previous frame is calculated.
- A threshold is applied to highlight areas with significant motion.

Alarm Trigger:

- If the sum of the thresholded differences exceeds a set value consistently, the alarm counter increases.
- When the counter exceeds a specific limit, the alarm is triggered using winsound.Beep.

Threading:

- The alarm sound is played on a separate thread to avoid blocking the main thread.
