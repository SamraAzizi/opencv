import cv2
import numpy as np

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Load target image
imgTarget = cv2.imread("cards.jpg")
if imgTarget is None:
    print("Error: Could not load target image.")
    exit()

hT, wT, cT = imgTarget.shape

# Initialize video capture for overlay video
myVideo = cv2.VideoCapture("flower.mp4")
if not myVideo.isOpened():
    print("Error: Could not open video file.")
    exit()

# Initialize ORB detector
orb = cv2.ORB_create(nfeatures=1000)

# Compute keypoints and descriptors for target image
kp1, des1 = orb.detectAndCompute(imgTarget, None)

# Draw keypoints on target image for visualization
imgTargetKeypoints = cv2.drawKeypoints(imgTarget, kp1, None)

while True:
    # Read frame from webcam
    successWebcam, imgWebcam = cap.read()
    if not successWebcam:
        print("Error: Could not read frame from webcam.")
        break

    # Read frame from video
    successVideo, imgVideo = myVideo.read()
    if not successVideo:
        # Restart video if it ends
        myVideo.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Resize video frame to match target image size
    imgVideoResized = cv2.resize(imgVideo, (wT, hT))

    # Compute keypoints and descriptors for webcam frame
    kp2, des2 = orb.detectAndCompute(imgWebcam, None)

    # Draw keypoints on webcam frame for visualization
    imgWebcamKeypoints = cv2.drawKeypoints(imgWebcam, kp2, None)

    # Display images
    cv2.imshow("Image Target Keypoints", imgTargetKeypoints)
    cv2.imshow("Video Frame Resized", imgVideoResized)
    cv2.imshow("Webcam Keypoints", imgWebcamKeypoints)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
myVideo.release()
cv2.destroyAllWindows()
