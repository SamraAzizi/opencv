
# Augmented Reality using OpenCV

This project demonstrates an augmented reality application using OpenCV. It uses a webcam to capture video frames, detects keypoints in the frames, and overlays a video on top of a target image.

## Requirements

* OpenCV 4.x
* NumPy
* A webcam
* A video file (e.g. "flower.mp4")
* A target image (e.g. "cards.jpg")

## Usage

1. Clone this repository and navigate to the project directory.
2. Install the required dependencies by running `pip install opencv-python numpy`.
3. Replace the `target_image` and `video_file` variables in the code with the paths to your own target image and video file.
4. Run the code by executing `python augmented_reality.py`.
5. The application will display several windows:
	* "Image Features": shows the target image with keypoints and matches.
	* "Webcam Keypoints": shows the webcam frame with keypoints.
	* "Video Frame Resized": shows the resized video frame.
	* "Image Target Keypoints": shows the target image with keypoints.
6. Press 'q' to exit the application.

## Code Explanation

The code uses the following steps to achieve augmented reality:

1. Initialize the webcam and video capture.
2. Load and resize the target image.
3. Compute keypoints and descriptors for the target image using ORB.
4. Read frames from the webcam and video.
5. Resize the video frame to match the target dimensions.
6. Compute keypoints and descriptors for the resized webcam frame.
7. Perform matching between descriptors using Brute-Force matcher.
8. Apply ratio test to filter good matches.
9. Draw matches on the images.
10. Display the images.
