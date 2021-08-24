import PySimpleGUI as sg      
from sound.sound import play_sound
import random
from CamDetect import play_cam , close_cam

mood_list =['Angry','Disgusted','Fearful','Happy','Neutral','Sad','Suprise']


def open_window():
    while True :
        sg.theme('LightGreen4')
        ttk_style = 'vista'

        layout = [[sg.Text('welcome to mood stabilizers')],        
                        [sg.Button('random sound'), sg.Cancel('cancel')],
                        [sg.Button('check mood')],
                        [sg.Button('play mood')],
                        [sg.Button('choose mood')]]      

        window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

        event, values = window.read()    
        
        if event == 'random sound':
            print(0)
            play_sound(random.choice(mood_list)) 
            print(1)
            window.close()
            print(2)


            
        elif event == 'check mood':
            window.close()
            open_cam()    

        elif event == 'play mood':
            window.close()
            play_mood()

        elif event == 'choose mood':
            window.close()
            choose_mood()    

        elif event == 'cancel' :
            layout = [[sg.Text('is that good or not')],        
                        [sg.Button('yes'), sg.Button('no')]] 
            window = sg.Window('rate', layout , margins=(100,100))    
            event, values = window.read() 
            if event == 'yes':
                sg.popup('thanks')
                break
            elif event == 'no':
                sg.popup('sorry about that')
                break       
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


def choose_mood():
    while True:
        sg.theme('LightGreen4')
        ttk_style = 'vista'

        layout = [[sg.Text('choose a mood')],        
                        [sg.Button('Angry'), sg.Cancel('cancel')],
                        [sg.Button('Happy')],
                        [sg.Button('Disgusted')],
                        [sg.Button('Fearful')],
                        [sg.Button('Neutral')],
                        [sg.Button('Sad')],
                        [sg.Button('Surprised')],

                        ]      

        window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

        event, values = window.read()    
        
        if event != 'cancel':
            play_sound(event)
        elif event == 'cancel': 
            layout = [[sg.Text('is that good or not')],        
                        [sg.Button('yes'), sg.Button('no')]] 
            window = sg.Window('rate', layout , margins=(100,100))    
            event, values = window.read() 
            if event == 'yes':
                sg.popup('thanks')
                break
            elif event == 'no':
                sg.popup('sorry about that')
                break
    window.close()    


def main_page():
    sg.theme('DarkBlue15')
    ttk_style = 'vista'
    layout = [[sg.Text('Mood-Stabilizers')],        
                    [sg.Button('start'), sg.Cancel('cancel')]]      

    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()    
    if event == 'start':
        open_window()
    elif event == 'cancel': 
        layout = [[sg.Text('is that good or not')],        
                    [sg.Button('yes'), sg.Button('no')]] 
        window = sg.Window('rate', layout , margins=(100,100))    
        event, values = window.read() 
        if event == 'yes':
            sg.popup('thanks')
        elif event == 'no':
            sg.popup('sorry about that')
    window.close()

  

main_page()