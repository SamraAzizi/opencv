import cv2

# Load and resize the image
image = cv2.imread("123.webp")
image = cv2.resize(image, (720, 640))

# Define models
face_pbtxt = "models/opencv_face_detector.pbtxt"
face_pb = "models/opencv_face_detector_uint8.pb"

age_prototxt = "models/age_deploy.prototxt"
age_model = "models/age_net.caffemodel"  # Corrected extension

gender_prototxt = "models/gender_deploy.prototxt"
gender_model = "models/gender_net.caffemodel"  # Corrected extension

MODEL_MEAN_VALUES = [104, 117, 123]

# Load models
face = cv2.dnn.readNet(face_pb, face_pbtxt)
age = cv2.dnn.readNet(age_model, age_prototxt)
gen = cv2.dnn.readNet(gender_model, gender_prototxt)

# Setup classifications
age_classifications = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '25-32', '(38-43)', '(48-53)', '60-100']
gender_classifications = ['Male', 'Female']

# Copy the image
img_cp = image.copy()

# Get image dimensions and blob
img_h, img_w = img_cp.shape[:2]
blob = cv2.dnn.blobFromImage(img_cp, 1.0, (300, 300), MODEL_MEAN_VALUES, swapRB=True, crop=False)

# Perform face detection
face.setInput(blob)
detected_faces = face.forward()

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

for face_bound in face_bounds:
    try:
        face = img_cp[max(0, face_bound[1] - 15): min(face_bound[30] + 15, img_cp.shape[0]-1),
                      max(0, face_bound[0] - 15) : min(face_bound[2] + 15, img_cp.shape[1]-1)]
        

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 277), )

    except Exception as e:
        print(e)
        continue




# Display the result
cv2.imshow("result", img_cp)
while True:
    key = cv2.waitKey(10)
    if key == 27:  # ESC key to exit
        break

cv2.destroyAllWindows()
