import cv2

image = cv2.imread("123.webp")
image = cv2.resize(image, (720, 640))


#define modules
 
face_pbtxt = "models/opencv_face_detector.pbtxt"
face_pb = "models/opencv_face_detector_uint8.pb"