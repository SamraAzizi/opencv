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

plt.figure(figsize= (12,12))
for i in range(1, 10, 1):
    