import PySimpleGUI as sg      

def open_window():
    sg.theme('DarkAmber')
    ttk_style = 'vista'

    layout = [[sg.Text('Listen according to your mood')],        
                    [sg.Button('start listen'), sg.Cancel()]]      

    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()   
         

    window.close()

def main_page():
    sg.theme('DarkAmber')
    ttk_style = 'vista'
    layout = [[sg.Text('Mood-Stabilizers', font='Default 20')],        
                    [sg.Button('start'), sg.Exit()]]      
    window = sg.Window('Mood-Stabilizers', layout , margins=(300,200),ttk_theme=ttk_style)    

    event, values = window.read()    
    if event == 'start':
        open_window()
    window.close()
    
main_page()

