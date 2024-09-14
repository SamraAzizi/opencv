**Emotion Detector using Keras and OpenCV**
=====================================================

**Description**
---------------

This is a real-time emotion detector that uses a pre-trained Keras model to classify emotions from facial expressions. The detector uses OpenCV to capture video from the webcam, detect faces, and extract regions of interest (ROIs) for emotion classification.

**Requirements**
---------------

* Python 3.x
* Keras
* OpenCV
* Pre-trained Keras model (model.h5)
* Haar cascade classifier for face detection (haarcascade_frontalface_default.xml)

**Usage**
---------

1. Install the required libraries by running `pip install keras opencv-python`.
2. Place the pre-trained Keras model (model.h5) and the Haar cascade classifier (haarcascade_frontalface_default.xml) in the same directory as the script.
3. Run the script using Python (e.g., `python emotion_detector.py`).
4. The script will start capturing video from the webcam and display the detected emotions in real-time.
5. Press 'q' to exit the script.

**Code Explanation**
-------------------

The code consists of the following steps:

* Load the face classifier and the pre-trained Keras model.
* Define the labels for the emotions.
* Start capturing video from the webcam.
* Detect faces in each frame using the Haar cascade classifier.
* Extract the ROI of each face and resize it to the required size.
* Normalize the ROI and convert it to an array.
* Predict the emotion using the pre-trained Keras model.
* Display the detected emotion on the frame.

**Note**
------

<<<<<<< HEAD
This script assumes that the pre-trained Keras model is trained on a dataset with the following emotion labels: ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']. You may need to modify the script if your model is trained on a different dataset.
=======
This script assumes that the pre-trained Keras model is trained on a dataset with the following emotion labels: ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']. You may need to modify the script if your model is trained on a different dataset.
>>>>>>> 1db389f0a3bf8172b6e146257c02f9cac1b5a934
