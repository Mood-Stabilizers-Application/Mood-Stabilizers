from tkinter import *
import pygame


def play_sound(mood):
    root = Tk()

    root.geometry('300x300')

    root.title('Songs list')
    pygame.mixer.init()

    def play():
        pygame.mixer.music.load(f'MoodStablizer/sound/music/{mood}/{mood}.wav')
        pygame.mixer.music.play(loops=0)

    def stop():
        pygame.mixer.music.stop()

    bt_sraet = Button(root, text='Play', font=(22), command=play)
    bt_sraet.pack(pady=20)

    bt_stop = Button(root, text='Stop', font=(22), command=stop)
    bt_stop.pack(pady=20)

    # root.mainloop()
    return f'MoodStablizer/sound/music/{mood}/{mood}.wav'
