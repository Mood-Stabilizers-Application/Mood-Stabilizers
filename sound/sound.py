from playsound import playsound


def play_sound(mood):

    count = 1
    while count < 3:
        playsound('sound/music/angry/angry1.mp3')
        count += 1


play_sound('sad')
