from playsound import playsound
     
def play_sound(mood):
    playsound(f'sound/music/{mood}/{mood}.mp3')
    return f'sound/music/{mood}/{mood}.mp3'

play_sound('sad')