# Emotion Detection Using OpenCV and Keras

This project is a real-time emotion detection system using a webcam. It uses OpenCV for face detection and a pre-trained Keras model to classify emotions from facial expressions.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- Keras
- TensorFlow
- NumPy

You can install the required packages using pip:

```bash
pip install opencv-python keras tensorflow numpy

## How to Run

1. Clone the repository or download the files to your local machine.

2. Ensure that the paths in the Python script (`emotion_detection.py`) are correctly set for:
   - The Haar Cascade file (`haarcascade_frontalface_default.xml`).
   - The pre-trained Keras model (`model.h5`).

3. Run the script using Python:

   ```bash
   python emotion_detection.py
