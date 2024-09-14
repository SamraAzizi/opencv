from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

# Load the face classifier and the trained model
face_classifier = cv2.CascadeClassifier(r'C:\Users\CPCM\OneDrive\Desktop\opencv\emotionDetection\haarcascade_frontalface_default.xml')
classifier = load_model(r'C:\Users\CPCM\OneDrive\Desktop\opencv\emotionDetection\model.h5')

# Define the labels for the emotions
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break  # Exit if the frame was not captured successfully

    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)  # Detect faces

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

        # Extract the region of interest (ROI) of the face in grayscale
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)  # Resize to the required size

        if np.sum(roi_gray) != 0:  # Check if ROI is not empty
            roi = roi_gray.astype('float32') / 255.0  # Normalize the image
            roi = img_to_array(roi)  # Convert to array
            roi = np.expand_dims(roi, axis=0)  # Expand dimensions to match the model input shape

            # Predict the emotion
            prediction = classifier.predict(roi)[0]
            label = emotion_labels[prediction.argmax()]  # Get the label with the highest probability
            label_position = (x, y - 10)  # Position the label above the face

            # Display the label on the frame
            cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            # Display a message if no face is detected
            cv2.putText(frame, "No face found", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with the detected emotions
    cv2.imshow("Emotion Detector", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
