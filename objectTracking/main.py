import cv2

# Provide the full path to the video file if it's not in the same directory
cap = cv2.VideoCapture("C:\\Users\\CPCM\\OneDrive\\Desktop\\opencv\\objectTracking\\highway1.mp4")

#object detection from stable camera

object_detector = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()

    if not ret:
        break  # break the loop if the frame cannot be read

    mask = object_detector.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask" ,mask)

    # Add a delay to give the window a chance to display the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()