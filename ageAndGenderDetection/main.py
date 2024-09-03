import cv2

image = cv2.imread("123.webp")
image = cv2.resize(image, (720, 640))


#define models
 
face_pbtxt = "models/opencv_face_detector.pbtxt"
face_pb = "models/opencv_face_detector_uint8.pb"

age_prototxt = "models/age_deploy.prototxt"
age_model = "models/age_net.craffmodel"

gender_prototxt = "models/gender_deploy.prototxt"
gender_model = "models/gender_net.caffmodel"

#load models

face = cv2.dnn.readNet(face_pb, face_pbtxt)
age = cv2.dnn.readNet(age_model, age_prototxt)
gen = cv2.dnn.readNet(gender_model, gender_prototxt)

#setup classifications

age_classification = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '25-32']