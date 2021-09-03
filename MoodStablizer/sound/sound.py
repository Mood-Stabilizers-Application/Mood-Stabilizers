
from tkinter import *
import pygame

def paly_sound_path(mood):
    return f'MoodStablizer/sound/music/{mood}/{mood}.wav'
    
def play_sound(mood):
    root = Tk()

    root.geometry('300x300')

    root.title('songs')
    pygame.mixer.init()

    def play():
        pygame.mixer.music.load(paly_sound_path(mood))
        pygame.mixer.music.play(loops=0)

    def stop():
        pygame.mixer.music.stop()
        

    bt_sraet = Button(root , text='play',font=(22),command=play)
    bt_sraet.pack(pady=20)

    bt_stop = Button(root,text='stop',font=(22),command=stop)
    bt_stop.pack(pady=20)

    root.mainloop()