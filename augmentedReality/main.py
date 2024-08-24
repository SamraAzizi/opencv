import cv2
import numpy as np

# Set target dimensions for resizing
target_width = 640
target_height = 480

# Initialize webcam capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load and resize the target image
imgTarget = cv2.imread("C:/Users/CPCM/OneDrive/Desktop/opencv/augmentedReality/cards.jpg")
if imgTarget is None:
    print("Error: Could not load target image.")
    exit()
imgTarget = cv2.resize(imgTarget, (target_width, target_height))
hT, wT, cT = imgTarget.shape

# Initialize video capture for overlay video
myVideo = cv2.VideoCapture("C:/Users/CPCM/OneDrive/Desktop/opencv/augmentedReality/flower.mp4")
if not myVideo.isOpened():
    print("Error: Could not open video file.")
    exit()

# Initialize ORB detector
orb = cv2.ORB_create(nfeatures=1000)

# Compute keypoints and descriptors for the target image
kp1, des1 = orb.detectAndCompute(imgTarget, None)

# Draw keypoints on the target image for visualization
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

    # Resize video frame to match the target dimensions
    imgVideoResized = cv2.resize(imgVideo, (wT, hT))

    # Resize webcam frame to match the target dimensions
    imgWebcamResized = cv2.resize(imgWebcam, (wT, hT))

    # Compute keypoints and descriptors for the resized webcam frame
    kp2, des2 = orb.detectAndCompute(imgWebcamResized, None)

    # Draw keypoints on the resized webcam frame for visualization
    imgWebcamKeypoints = cv2.drawKeypoints(imgWebcamResized, kp2, None)

    bf = cv2.BFMatcher()
    matches = bf.KnnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n .distance:
            good.append(m)

    print(len(good))

    imgFeatures = cv2.drawMatches(imgTarget, kp1, imgWebcam, kp2, good, None, flags= 2)


    

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
