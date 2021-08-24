import PySimpleGUI as sg
from sound.sound import play_sound
import random
from CamDetect import play_cam, close_cam
mood_list = ['Angry', 'Disgusted', 'Fearful',
             'Happy', 'Neutral', 'Sad', 'Suprise']
after_quit = 'Did you like your experience with Mood Stabilizer?'
quit_yes_answer = 'thank you '
quit_no_answer = 'sorry to hear that'
def open_window():
    while True:
        sg.theme('LightGreen4')
        ttk_style = 'vista'
        layout = [[sg.Text('welcome to Mood stabilizers')],
                  [sg.Button('lestin to a random song from the library'),
                   sg.Cancel('quit')],
                  [sg.Button('what is my currunt Mood?')],
                  [sg.Button('Know your mood and let us make you feel better.')],
                  [sg.Button('pick your mood manually')]]
        window = sg.Window('Mood-Stabilizers', layout,
                           margins=(300, 200), ttk_theme=ttk_style)
        event, values = window.read()
        if event == 'lestin to a random song from the library':
            print(0)
            play_sound(random.choice(mood_list))
            print(1)
            window.close()
            print(2)
        elif event == 'what is my currunt Mood?':
            window.close()
            open_cam()
        elif event == 'Know your mood and let us make you feel better.':
            window.close()
            play_mood()
        elif event == 'pick your mood manually':
            window.close()
            choose_mood()
        elif event == 'quit':
            layout = [[sg.Text(after_quit)],
                      [sg.Button('yes'), sg.Button('no')]]
            window = sg.Window('rate', layout, margins=(100, 100))
            event, values = window.read()
            if event == 'yes':
                sg.popup(quit_yes_answer)
                break
            elif event == 'no':
                sg.popup(quit_no_answer)
                break
    window.close()
def open_cam():
    sg.theme('LightGreen4')
    ttk_style = 'vista'
    layout = [[sg.Text('welcome to mood stabilizers')],
              [sg.Button('what is my currunt Mood?'), sg.Cancel()],
              ]
    window = sg.Window('Mood-Stabilizers', layout,
                       margins=(300, 200), ttk_theme=ttk_style)
    event, values = window.read()
    if event == 'what is my currunt Mood?':
        mood = play_cam()
        sg.popup(f'your mood is {mood}')
    window.close()
def play_mood():
    sg.theme('LightGreen4')
    ttk_style = 'vista'
    layout = [[sg.Text('welcome to mood stabilizers')],
              [sg.Button(
                  'Know your mood and let us make you feel better.'), sg.Cancel()],
              ]
    window = sg.Window('Mood-Stabilizers', layout,
                       margins=(300, 200), ttk_theme=ttk_style)
    event, values = window.read()
    if event == 'Know your mood and let us make you feel better.':
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
                  [sg.Button('Angry'), sg.Cancel('quit')],
                  [sg.Button('Happy')],
                  [sg.Button('Disgusted')],
                  [sg.Button('Fearful')],
                  [sg.Button('Neutral')],
                  [sg.Button('Sad')],
                  [sg.Button('Surprised')],
                  ]
        window = sg.Window('Mood-Stabilizers', layout,
                           margins=(300, 200), ttk_theme=ttk_style)
        event, values = window.read()
        if event != 'quit':
            play_sound(event)
        elif event == 'quit':
            layout = [[sg.Text(after_quit)],
                      [sg.Button('yes'), sg.Button('no')]]
            window = sg.Window('rate', layout, margins=(100, 100))
            event, values = window.read()
            if event == 'yes':
                sg.popup(quit_yes_answer)
                break
            elif event == 'no':
                sg.popup(quit_no_answer)
                break
    window.close()
def main_page():
    sg.theme('DarkBlue15')
    ttk_style = 'vista'
    layout = [[sg.Text('Mood-Stabilizers')],
              [sg.Button('start'), sg.Cancel('quit')]]
    window = sg.Window('Mood-Stabilizers', layout,
                       margins=(300, 200), ttk_theme=ttk_style)
    event, values = window.read()
    if event == 'start':
        open_window()
    elif event == 'quit':
        layout = [[sg.Text(after_quit)],
                  [sg.Button('yes'), sg.Button('no')]]
        window = sg.Window('rate', layout, margins=(100, 100))
        event, values = window.read()
        if event == 'yes':
            sg.popup(quit_yes_answer)
        elif event == 'no':
            sg.popup(quit_no_answer)
    window.close()
main_page()