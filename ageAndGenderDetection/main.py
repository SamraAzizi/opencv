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
MODEL_MEAN_VALUES = [104, 117, 123]

#load models

face = cv2.dnn.readNet(face_pb, face_pbtxt)
age = cv2.dnn.readNet(age_model, age_prototxt)
gen = cv2.dnn.readNet(gender_model, gender_prototxt)

#setup classifications

age_classifications = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '25-32','(38-43)','(48-53)','60-100']
gender_classifications = ['Male','Female'] 

#copy image

img_cp = image.copy()

#get images dimension and blob

img_h = img_cp.shape[0]
img_w = img_cp.shape[1]
blob = cv2.dnn.blobFromImage(img_cp, 1, 0, (300, 300),MODEL_MEAN_VALUES, True, False)


face.setInput(blob)
detected_faces = face.forward()

face_bounds =  []

#draw rectangle over face

for i in range(detected_faces.shape[2]):
    confidence = detected_faces[0,0,i,2]
    if (confidence > 0.99):
        x1 = detected_faces[0,0,i,3] * img_w
        x2 = detected_faces[0,0,i,4] * img_w
         
    