import matplotlib.pyplot as plt
import numpy as np
import pandas as np
import seaborn as sns
import os

# importing Deep Learning Libraries

from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Input, Dropout, GlobalAveragePooling2D, Flatten, Conv2D, BatchNormalization, Activation, MaxPooling2
from keras.model import Model, Sequentail
from keras.optimizers import Adam, SGD, RMprop

#display images

picture_size = 48
folder_path = ""

expression = 'disgust'
plt.style.use('dark_background')
plt.figure(figsize= (12,12))
for i in range(1, 10, 1):
    plt.subplot(3,3,i)
    img = load_img(folder_path+"train/"+expression+"/"+
                   os.listdir(folder_path+"train/" + expression)[i], target_size= (picture_size, picture_size))
    plt.imshow(img)

plt.show()