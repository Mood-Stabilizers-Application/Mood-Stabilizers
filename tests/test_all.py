import pygame
from sound.sound import *
from MoodStablizer.CamDetect import time
import cv2
import datetime
from MoodStablizer.machine_test import *
import numpy as np



def test_play_sound():
    excepted = 'sound/music/Sad/Sad.wav'
    actual = paly_sound_path('Sad')
    assert excepted == actual


def test_convert_image():
    x = cv2.imread('data/images.jpeg')
    gray_frame = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    excepted=x
    actual=gray_frame
    assert excepted == actual

def test_resize_image():
    x=cv2.imread('data/images.jpeg')
    gray_frame = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    cropped_img = np.expand_dims(
                np.expand_dims(cv2.resize(gray_frame, (48, 48)), -1), 0
            )
    actual=cropped_img
    excepted=x
    assert excepted == actual

            





# def test_cam():
#     cap = cv2.VideoCapture(0)
#     excepted = True
#     actual = cap.isOpened()
#     actual = True
#     assert excepted == actual


def test_time():
    excepted = datetime.datetime.now().second + 5
    actual = time()
    assert excepted == actual


# def test_images():
#     excepted = (
#         'number of train images is:28709 and number of validation images is: 3422')

#     actual = images()
#     assert excepted == actual


# def test_model():
#     excepted = 'dense_3/Softmax:0'

#     actual = model()
#     assert excepted == actual
