import pygame
from sound.sound import *
from MoodStablizer.CamDetect import time
import cv2
import datetime
from MoodStablizer.machine_test import *


def test_play_sound():
    excepted = 'sound/music/Sad/Sad.wav'
    actual = paly_sound_path('Sad')
    assert excepted == actual


def test_cam():
    cap = cv2.VideoCapture(0)
    excepted = True
    actual = cap.isOpened()
    actual = True
    assert excepted == actual


def test_time():
    excepted = datetime.datetime.now().second + 5
    actual = time()
    assert excepted == actual


# def test_images():
#     excepted = (
#         'number of train images is:12966 and number of validation images is: 3422')

#     actual = images()
#     assert excepted == actual


# def test_model():
#     excepted = 'dense_1/Softmax:0'

#     actual = model()
#     assert excepted == actual
