# Object Tracking using OpenCV

This project demonstrates object tracking using a webcam or video file. It uses OpenCV for video processing and tracking objects based on Euclidean distance.

## Features

- Detects and tracks objects from a stable camera
- Draws bounding boxes and IDs around detected objects
- Real-time tracking

## Requirements

- Python 3.x
- OpenCV

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/object-tracking.git
    ```

2. Navigate to the project directory:

    ```bash
    cd object-tracking
    ```

3. Install the required library:

    ```bash
    pip install opencv-python
    ```

## Usage

1. Ensure your video file is available. Provide the full path to the video file if it's not in the same directory.

2. Run the script:

    ```bash
    python main.py
    ```

## Notes

- Make sure to replace the path in `cap = cv2.VideoCapture("C:\\Users\\CPCM\\OneDrive\\Desktop\\opencv\\objectTracking\\highway1.mp4")` with the actual path to your video file.
- The `tracker.py` file should contain the `EuclidearDistTracker` class definition for tracking objects based on Euclidean distance.
