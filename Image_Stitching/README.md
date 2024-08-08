# Image Stitching Script

This Python script uses OpenCV to stitch multiple images together into a panorama. The images are read from a specified folder, resized, and processed to generate a single stitched image.

## Features

- **Automatic Image Stitching**: Combines multiple images into a single panoramic image.
- **Error Handling**: Provides feedback if stitching fails due to insufficient images, homography estimation issues, or camera parameter adjustments.
- **Image Resizing**: Images are resized to a smaller scale before stitching to reduce processing time.

## Prerequisites

- **Python 3.x**
- **OpenCV**: Install via pip if not already installed.
  
  ```bash
  pip install opencv-python



## Setup and Usage

1. **Folder Structure**:
   - Place the images you want to stitch into a folder named `Images` inside a directory named `Image_Stitching`. The folder structure should look like this:
   
     ```
     Image_Stitching/
     └── Images/
         ├── image1.jpg
         ├── image2.jpg
         └── ...
     ```

2. **Running the Script**:
   - 