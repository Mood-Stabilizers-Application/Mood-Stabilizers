
import numpy as np
from keras.models import load_model

def handle_image(cropped_img):
    emotion_model = load_model('MoodStablizer/emotion_model2.h5')
    # change the cropped img to an array the can be predected using the model
    emotion_prediction = emotion_model.predict(cropped_img)
    # emotion prediction as a number
    maxindex = int(np.argmax(emotion_prediction))
    # max index is the emotion index in emotion_dict
    return maxindex