import cv2
import os



# Define the main folder path
mainFolder = 'Image_Stitching/Images'

# Check if the main folder exists and is a directory
if not os.path.isdir(mainFolder):
    print(f"The path {mainFolder} is not a directory or does not exist.")
    exit(1)

# Get the list of files in the main folder
myFiles = os.listdir(mainFolder)

images = []
for file in myFiles:
    filePath = os.path.join(mainFolder, file)
    if os.path.isfile(filePath):
        print(f'Processing file: {filePath}')
        curImg = cv2.imread(filePath)
        if curImg is not None:
            curImg = cv2.resize(curImg, (0,0), fx=0.5, fy=0.5) 
            images.append(curImg)
        else:
            print(f"Failed to read image: {filePath}")
    else:
        print(f"Skipping non-file item: {filePath}")

if len(images) > 1:
    stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
    (status, result) = stitcher.stitch(images)
    if status == cv2.Stitcher_OK:
        print("Panorama generated")
        # Save the stitched image
        cv2.imwrite('stitched_image.jpg', result)
        # Display the stitched image
        cv2.imshow('Stitched Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Stitching failed with status code: {status}")
        if status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
            print("Need more images to stitch.")
        elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
            print("Homography estimation failed.")
        elif status == cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
            print("Camera parameters adjustment failed.")
else:
    print("Not enough images to stitch")
