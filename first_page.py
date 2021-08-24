import PySimpleGUI as sg      
from sound.sound import play_sound
import random
from CamDetect import play_cam , close_cam

mood_list =['angry','disgusted','Fearful','happy','neutral','sad','suprise']


def open_window():
    sg.theme('LightGreen4')
    ttk_style = 'vista'

    layout = [[sg.Text('welcome to mood stabilizers')],        
                    [sg.Button('random sound'), sg.Cancel()],
                    [sg.Button('check mood')],
                    [sg.Button('play mood')]]      

    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()    
     
    if event == 'random sound':
        play_sound(random.choice(mood_list)) 

    elif event == 'check mood':
        open_cam()    
    elif event == 'play mood':
        play_mood()


    window.close()

def open_cam():
    sg.theme('LightGreen4')
    ttk_style = 'vista'

    layout = [[sg.Text('welcome to mood stabilizers')],        
                    [sg.Button('check mood'), sg.Cancel()],
                    ]      

    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()    
     
    if event == 'check mood':
        mood =play_cam()
        sg.popup(f'your mood is {mood}')


    window.close()

def play_mood():
    sg.theme('LightGreen4')
    ttk_style = 'vista'

    layout = [[sg.Text('welcome to mood stabilizers')],        
                    [sg.Button('play mood'), sg.Cancel()],
                    ]      

    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()    
     
    if event == 'play mood':
        mood = play_cam()
        if mood:
           close_cam()
           sg.popup(f'your mood is {mood}')
           play_sound(mood)
        
    window.close()

def main_page():
    sg.theme('DarkBlue15')
    ttk_style = 'vista'
    layout = [[sg.Text('Mood-Stabilizers')],        
                    [sg.Button('start'), sg.Cancel()]]      

    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()    
    if event == 'start':
        open_window()
    window.close()

  

main_page()