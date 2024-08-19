import mediapipe as mp
import time
import cv2


class PoseDetector():
    def __init__(self, mode=False, upperBody=False, smooth=True, 
                 detectionCon=0.5, trackCon=0.5):
        
        self.mode = mode
        self.upperBody = upperBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose

        self.pose = self.mpPose.Pose(static_image_mode=self.mode, 
                                     model_complexity=self.upperBody, 
                                     smooth_landmarks=self.smooth, 
                                     min_detection_confidence=self.detectionCon, 
                                     min_tracking_confidence=self.trackCon)

    def findPose(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
                
        return img


    def findPosition(self, img, draw=True):
        lmList = []

        if self.results.pose_landmarks:

            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape

                cx, cy = int(lm.x *w ), int( lm.y* h)
                lmList.append([id, cx, cy])
                if draw: 
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return lmList



def main():
    cap = cv2.VideoCapture(r"C:\Users\CPCM\OneDrive\Desktop\opencv\poseEstimation\123.mp4")

    prevTime = 0
    detector = PoseDetector()

    while True:

        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if lmList:
            cv2.circle(img, (lmList[1][1], lmList[1][2]), 5, (255, 0, 0), cv2.FILLED)

        currentTime = time.time()
        fps = 1/(currentTime - prevTime)
        prevTime = currentTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()