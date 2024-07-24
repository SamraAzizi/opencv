import cv2

# Provide the full path to the video file if it's not in the same directory
cap = cv2.VideoCapture("C:\\Users\\CPCM\\OneDrive\\Desktop\\opencv\\objectTracking\\highway1.mp4")

#object detection from stable camera

object_detector = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()

    #extract regionof interest

    height, width , _ = frame.shape
    print(height, width)

    if not ret:
        break  # break the loop if the frame cannot be read

    #object detection

    mask = object_detector.apply(frame)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        #calculate area nad remove small elements

        area = cv2.contourArea(cnt)

        if area < 100:

            cv2.drawContours(frame, [cnt], -1, (0,255,0), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask" ,mask)

    # Add a delay to give the window a chance to display the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()