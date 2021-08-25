from sound.sound import paly_sound_path
from MoodStablizer.CamDetect import time
import cv2
import datetime


def test_play_sound():
    excepted = 'sound/music/Sad/Sad.wav'
    actual = paly_sound_path('Sad')
    assert excepted == actual


def test_cam():
    cap = cv2.VideoCapture(0)
    excepted = True
    actual = cap.isOpened()
    assert excepted == actual


def test_time():
    excepted = datetime.datetime.now().second + 5
    actual = time()
    assert excepted == actual
