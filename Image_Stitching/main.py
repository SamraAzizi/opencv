import cv2
import os

# Define the main folder path
mainFolder = 'Image_Stitching/Images'

# Get the list of files in the main folder
myFiles = os.listdir(mainFolder)

images = []
for file in myFiles:
    filePath = os.path.join(mainFolder, file)
    print(f'Processing file: {filePath}')
    curImg = cv2.imread(filePath)
    curImg = cv2.resize(curImg, (0,0), None, 0.2, 0.2)
    images.append(curImg)

stitcher = cv2.Stitcher.create()
(status, result) = stitcher.stitch(images)
if(status == cv2.STITCHER_OK):
    print("Panorama generated")
else:
    print("Unsuccessful generation")