import PySimpleGUI as sg      
from sound.sound import play_sound
import random

mood_list =['angry','disgusted','Fearful','happy','neutral','sad','suprise']


def open_window():
    sg.theme('LightGreen4')
    ttk_style = 'vista'

    layout = [[sg.Text('welcome to mood stabilizers')],        
                    [sg.Button('click to listen to random sound'), sg.Cancel()]]      

    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()    
     
    if event :
        play_sound(random.choice(mood_list)) 
        

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