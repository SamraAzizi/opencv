# Eye Detection using OpenCV and Dlib

This project demonstrates eye detection using a webcam feed with OpenCV and Dlib's face landmark detector. The program captures real-time video, detects faces, and then identifies the eyes using specific facial landmarks.

## Prerequisites

Before running this code, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV
- NumPy
- Dlib

You can install these dependencies using pip:

```bash
pip install opencv-python numpy dlib
```

# Setup

1. **Dlib's Shape Predictor**: This code requires the `shape_predictor_68_face_landmarks.dat` file, 
   which contains the trained model to detect facial landmarks. 
   You can download it from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 and extract the file.

2. **Update the Path**: Ensure the path to the `shape_predictor_68_face_landmarks.dat` file in the code is correctly set:
   
   predictor = dlib.shape_predictor(r"C:\\Users\\CPCM\\OneDrive\\Desktop\\opencv\\eyeDetection\\shape_predictor_68_face_landmarks.dat")

# How It Works

- The code starts by capturing video from the default webcam.
- It then converts each frame to grayscale for easier processing.
- Using Dlib's face detector, it detects any faces in the frame.
- For each detected face, the code locates specific facial landmarks (specifically around the eyes).
- It draws horizontal and vertical lines across the eyes to visualize the detection.

# Usage

1. Ensure your webcam is connected and accessible.
2. Run the script:

   python eye_detection.py

3. The webcam feed will open, showing the detected eyes with lines drawn across them.
4. Press `Esc` to exit the program.

