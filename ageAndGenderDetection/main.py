import cv2
import os

# Change working directory to models directory
os.chdir('C:\\Users\\CPCM\\OneDrive\\Desktop\\opencv\\ageAndGenderDetection\\models')

# Define image and model paths
image_path = r"C:\Users\CPCM\OneDrive\Desktop\opencv\ageAndGenderDetection\hey.webp"
face_pbtxt = os.path.join(os.getcwd(), "opencv_face_detector.pbtxt")
face_pb = os.path.join(os.getcwd(), "opencv_face_detector_uint8.pb")
age_prototxt = os.path.join(os.getcwd(), "age_deploy.prototxt")
age_model = os.path.join(os.getcwd(), "age_net.caffemodel")
gender_prototxt = os.path.join(os.getcwd(), "gender_deploy.prototxt")
gender_model = os.path.join(os.getcwd(), "gender_net.caffemodel")
MODEL_MEAN_VALUES = [104, 117, 123]

# Check if image file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file '{image_path}' not found. Please check the file path.")

# Load and check the image
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not load the image from '{image_path}'. Please check the file format and integrity.")

# Resize the image
image = cv2.resize(image, (720, 640))

# Check if model files exist
for model in [face_pb, age_model, gender_model]:
    if not os.path.exists(model):
        raise FileNotFoundError(f"Model file '{model}' not found. Please check the file path.")

# Load models
face_net = cv2.dnn.readNetFromTensorflow(face_pb, face_pbtxt)
age_net = cv2.dnn.readNetFromCaffe(age_prototxt, age_model)
gender_net = cv2.dnn.readNetFromCaffe(gender_prototxt, gender_model)

# Setup classifications
age_classifications = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '25-32', '(38-43)', '(48-53)', '60-100']
gender_classifications = ['Male', 'Female']

# Copy the image
img_cp = image.copy()

# Get image dimensions and blob
img_h, img_w = img_cp.shape[:2]
blob = cv2.dnn.blobFromImage(img_cp, 1.0, (300, 300), MODEL_MEAN_VALUES, swapRB=True, crop=False)

# Perform face detection
face_net.setInput(blob)
detected_faces = face_net.forward()

face_bounds = []

# Draw rectangles over detected faces
for i in range(detected_faces.shape[2]):
    confidence = detected_faces[0, 0, i, 2]
    if confidence > 0.99:
        x1 = int(detected_faces[0, 0, i, 3] * img_w)
        y1 = int(detected_faces[0, 0, i, 4] * img_h)
        x2 = int(detected_faces[0, 0, i, 5] * img_w)
        y2 = int(detected_faces[0, 0, i, 6] * img_h)

        cv2.rectangle(img_cp, (x1, y1), (x2, y2), (0, 255, 0), int(round(img_h / 150)), 8)
        face_bounds.append([x1, y1, x2, y2])

if not face_bounds:
    raise RuntimeError("No faces were detected.")

# Perform age and gender prediction
for face_bound in face_bounds:
    try:
        face = img_cp[max(0, face_bound[1] - 15): min(face_bound[3] + 15, img_cp.shape[0] - 1),
                      max(0, face_bound[0] - 15): min(face_bound[2] + 15, img_cp.shape[1] - 1)]

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

        # Predict gender
        gender_net.setInput(blob)
        gender_predict = gender_net.forward()
        gender = gender_classifications[gender_predict[0].argmax()]

        # Predict age
        age_net.setInput(blob)
        age_predict = age_net.forward()
        age = age_classifications[age_predict[0].argmax()]

        # Draw text on the image
        cv2.putText(img_cp, f'{gender}, {age}', (face_bound[0], face_bound[1] + 10), 
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 4, cv2.LINE_AA)

    except Exception:
        continue

# Display the result
cv2.imshow("result", img_cp)
try:
    while True:
        key = cv2.waitKey(10)
        if key == 27:  # ESC key to exit
            break
finally:
    cv2.destroyAllWindows()
