# Face Detection using OpenCV

This project demonstrates basic face detection using OpenCV's Haar Cascades.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV (`opencv-python` package)

## Installation

1. Clone the repository or download the script files.
2. Install the necessary Python packages using pip:
    ```bash
    pip install opencv-python
    ```

## Setup

Make sure you have the Haar Cascade XML file (`haarcascade_frontalface_default.xml`). You can download it from the official OpenCV GitHub repository: https://github.com/opencv/opencv/tree/master/data/haarcascades

Save the XML file in your project directory.

## Usage

1. Create a Python script (e.g., `face_detection.py`) with the following content:

    ```python
    import cv2

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread('input.jpg')

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```

2. Replace `'input.jpg'` with the path to your image file.

3. Run the script:
    ```bash
    python face_detection.py
    ```

## Notes

- Make sure the image file path is correct.
- Adjust the `detectMultiScale` parameters for better accuracy if needed.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License.
