
import mediapipe as mp
import time
import cv2

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose

pose = mpPose.Pose()

cap = cv2.VideoCapture(r"C:\Users\CPCM\OneDrive\Desktop\opencv\poseEstimation\123.mp4")

prevTime = 0

while True:

    success, img = cap.read()

    if not success:
        print("Failed to read frame. Exiting...")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape

            cx, cy = int(lm.x *w ), int( lm.y* h)
            cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)



    currentTime = time.time()
    fps = 1/(currentTime - prevTime)
    prevTime = currentTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
