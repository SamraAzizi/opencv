import cv2

image = cv2.imread("123.webp")
image = cv2.resize(image, (720, 640))


#define modules
 
face_pbtxt = "models/opencv_face_detector.pbtxt"
face_pb = "models/opencv_face_detector_uint8.pb"

age_prototxt = "models/age_deploy.prototxt"
age_model = "models/age_net.craffmodel"

gender_prototxt = "models/gender_deploy.prototxt"
gender_model = "models/gender_net.caffmodel"