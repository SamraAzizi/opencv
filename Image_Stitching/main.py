import cv2
import os


mainFolder = "Images"
myFolders = os.listdir(mainFolder)


for folder in myFolders:
    path = mainFolder + '/'+folder
    images = []
    myList = os.listdir(path)

    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        images.append(curImg)
