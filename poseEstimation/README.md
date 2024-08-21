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
  - `PoseDetector` class 
