from MoodStablizer.sound.sound import *
from MoodStablizer.CamDetect import *
import cv2
import datetime


def test_load_img_index():
    img = cv2.imread('images.jpeg')
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cropped_img = np.expand_dims(
                    np.expand_dims(cv2.resize(gray_frame, (48, 48)), -1), 0
                )
    excepted = 4 
    actual = load_img(cropped_img)
    assert excepted == actual



def test_load_img_mood():
    img = cv2.imread('images.jpeg')
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cropped_img = np.expand_dims(
                    np.expand_dims(cv2.resize(gray_frame, (48, 48)), -1), 0
                )
    excepted = 'Neutral'
    index = load_img(cropped_img)
    actual = emotion_dict[index]
    assert excepted == actual



def test_play_sound():
    excepted = 'sound/music/Sad/Sad.wav'
    actual = paly_sound_path('Sad')
    assert excepted == actual



def test_time():
    excepted = datetime.datetime.now().second + 5
    actual = time()
    assert excepted == actual


