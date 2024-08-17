
import mediapipe as mp
import time
import opencv

mpPose = mp.solutions.pose

pose = mpPose.Pose()

cap = cv2.VideoCapture("")
prevTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2GB)
    results = pose.process(imgRGB)
    

    currentTime = time.time()
    fps = 1/(currentTime - prevTime)
    prevTime = currentTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0),3)
                                
                                
    cv2.imshow("Image", img)
    cv2.waitKey(1)