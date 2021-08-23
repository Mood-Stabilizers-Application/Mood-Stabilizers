# Import all packages and libraries
from MoodStablizer.train import *

# Code for GUI and mapping with emojis

# start the webcam feed
cap = cv2.VideoCapture(0)
while True:
    # Find haarcascade to draw bounding box around face
    ret, frame = cap.read()
    if not ret:
        break
    bounding_box = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    num_faces = bounding_box.detectMultiScale(
        gray_frame, scaleFactor=1.3, minNeighbors=5
    )