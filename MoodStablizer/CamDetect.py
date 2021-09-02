import cv2
import numpy as np
from keras.models import load_model
import datetime
from MoodStablizer.handel_image import *
from time_capture import *
from play_cam import *


time()

handle_image()

play_cam()


close_cam()

    
# play_cam()


x = cv2.imread('data/images.jpeg')
# print(x)
gray_frame = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
cropped_img = np.expand_dims(
                np.expand_dims(cv2.resize(gray_frame, (48, 48)), -1), 0
            )
            
print(handle_image(cropped_img))
print(handle_image(cropped_img))