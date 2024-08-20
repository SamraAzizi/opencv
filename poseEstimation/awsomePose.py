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