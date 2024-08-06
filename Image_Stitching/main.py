import cv2
import os


mainFolder = "Images"
myFolders = os.listdir(mainFolder)
 for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        curImg = cv2.resize(curImg, (0,0), None, 0.2, 0.2)
        images.append(curImg)

for folder in myFolders:
    path = mainFolder + '/'+folder
    images = []
    myList = os.listdir(path)

   


    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
