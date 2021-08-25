import cv2
import numpy as np
from keras.models import load_model
import datetime


def time():
    time_1 = datetime.datetime.now().second
    time_2 = time_1 + 5
    return time_2


def play_cam():

    emotion_model = load_model('MoodStablizer/emotion_model2.h5')

    emotion_dict = {
        0: "Angry",
        1: "Disgusted",
        2: "Fearful",
        3: "Happy",
        4: "Neutral",
        5: "Sad",
        6: "Surprised",
    }
    cap = cv2.VideoCapture(0)
    time_2 = time()
    while True:
        ret, frame = cap.read()

        # print(ret) is boolean if it is exist it is True
        # print(frame) is frame as an array

        if not ret:
            break
        #  if ret is not exist(no frame) exit the loop
        bounding_box = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml"
        )
        #  this is the bounding box around my face

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #  in gray frame it changes the picture from the user to gray color

        num_faces = bounding_box.detectMultiScale(
            gray_frame, scaleFactor=1.3, minNeighbors=5
        )
        # print(num_faces)
        #  return vector of rectangles
        #  [[275 265 165 165]]

        for (x, y, w, h) in num_faces:
            cv2.rectangle(frame, (x, y - 50),
                          (x + w, y + h + 10), (255, 0, 0), 2)
            #  cv2.rectangle is used to draw a rectangle with  these coordinations
            # image = cv2.rectangle(image, start_point, end_point, color, thickness)

            roi_gray_frame = gray_frame[y: y + h, x: x + w]
            #  cut the face based on the rectangle coordinations
            cropped_img = np.expand_dims(
                np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0
            )
            # change the cropped img to an array the can be predected using the model
            emotion_prediction = emotion_model.predict(cropped_img)
            #  emotion prediction as a number
            maxindex = int(np.argmax(emotion_prediction))
            # max index is the emotion index in emotion_dict
            cv2.putText(
                frame,
                emotion_dict[maxindex],
                (x + 20, y - 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )
            # cv2.puttest add the text above the rectangle

        cv2.imshow("Video", cv2.resize(
            frame, (1200, 860), interpolation=cv2.INTER_CUBIC))
        #  cv2.imshow is opening the video
        if cv2.waitKey(1) and datetime.datetime.now().second == time_2:
            cap.release()
            cv2.destroyAllWindows()
            return emotion_dict[maxindex]

    cap.release()
    # Closes video file or capturing device.
    # The method is automatically called by subsequent VideoCapture::open and by VideoCapture destructor.

    cv2.destroyAllWindows()

    # Removing windows by calling below function


def close_cam():
    cv2.destroyAllWindows()
