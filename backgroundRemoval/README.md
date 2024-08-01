# Background Removal using OpenCV and MediaPipe

This project implements a background removal system using a webcam, OpenCV, and MediaPipe's Selfie Segmentation. The system replaces the background of the video feed with a specified image.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Requirements](#requirements)


## Installation

1. Clone this repository to your local machine:

```sh
git clone https://github.com/yourusername/background-removal.git
cd background-removal

```
## Features

- Replaces the background of the video feed with a specified image.
- Uses MediaPipe's Selfie Segmentation for accurate background removal.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy


## Usage

1. Place your background image in the specified path or update the `imgBg_path` variable in the code to point to your image:

```python
imgBg_path = "C:\\Users\\CPCM\\OneDrive\\Desktop\\opencv\\backgroundRemoval\\images\\hey.jpg"
