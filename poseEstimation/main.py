import opencv
import mediapipe as mp
import time


cap = cv2.VideoCapture("")
prevTime = 0

while True:
    success, img = cap.read()
    

    currentTime = time.time()
    fps = 1/(currentTime - prevTime)
    prevTime = currentTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0),3)
                                
                                
    cv2.imshow("Image", img)
    cv2.waitKey(1)