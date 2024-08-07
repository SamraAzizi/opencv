import cv2





import os

mainFolder = 'Image_Stitching/Images'

# Ensure 'mainFolder' is a directory
if os.path.isdir(mainFolder):
    # List all items in 'mainFolder'
    myList = os.listdir(mainFolder)
    print(myList)  # Prints the list of files in the directory

    for item in myList:
        itemPath = os.path.join(mainFolder, item)
        if os.path.isfile(itemPath):
            print(f"Processing file: {itemPath}")
           
        else:
            print(f"Skipping non-file item: {itemPath}")
else:
    print(f"The path {mainFolder} is not a directory.")

myFolders = os.listdir(mainFolder)


for folder in myFolders:
    path = mainFolder + '/'+folder
    images = []
    myList = os.listdir(path)

    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg, (0,0), None, 0.2, 0.2)
        images.append(curImg)


    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)