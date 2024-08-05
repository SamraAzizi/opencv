import cv2
import os


mainFolder = "Images"
myFolders = os.listdir(mainFolder)


for folder in myFolders:
    path = mainFolder + '/'+folder
    images = []
    myList = os.listdir(path)
