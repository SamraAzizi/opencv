# Pose Estimation with MediaPipe and OpenCV

## Overview

This project demonstrates three different implementations of pose estimation using MediaPipe and OpenCV. The code tracks and processes pose landmarks from a video file, displaying the results with real-time FPS (Frames Per Second) on the screen.

## File Descriptions

### 1. `pose_estimation_basic.py`

This file contains the simplest implementation of pose estimation using MediaPipe. It directly reads the video, processes the frames, and draws pose landmarks.

- **Features:**
  - Direct use of MediaPipe's `Pose` module.
  - Draws pose landmarks on each frame.
  - Displays real-time FPS on the video.

### 2. `pose_estimation_class.py`

This file enhances the basic implementation by encapsulating the pose estimation logic within a class called `PoseDetector`.

- **Features:**
  - `PoseDetector` class for better code organization and reusability.
  - Methods to find the pose and the positions of landmarks.
  - Allows toggling drawing of landmarks and more control over detection parameters.

### 3. `pose_estimation_main.py`

This file further builds on the class-based implementation. It imports the `PoseDetector` class from the second file and uses it in a streamlined main loop.

- **Features:**
  - Reuses the `PoseDetector` class for pose detection.
  - Demonstrates how to structure a
2. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe
