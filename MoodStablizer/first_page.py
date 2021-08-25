import PySimpleGUI as sg
from sound.sound import play_sound
import random
from CamDetect import play_cam, close_cam
mood_list = ['Angry', 'Disgusted', 'Fearful',
             'Happy', 'Neutral', 'Sad', 'Suprise']
after_quit = 'Did you like your experience with Mood Stabilizer?'
quit_yes_answer = 'thank you '
quit_no_answer = 'sorry to hear that'


def main_page():
    sg.theme('DarkAmber')
    ttk_style = 'vista'
    layout = [[sg.Text('Mood-Stabilizers')],
              [sg.Button('start'), sg.Cancel('quit')]]
    window = sg.Window('Mood-Stabilizers', layout,
                       margins=(250, 150), ttk_theme=ttk_style, size=(700, 400))
    event, values = window.read()
    print(values)
    print(event)
    if event == 'start':
        # pass
        window.close()
        open_window()
    elif event == 'quit' or event == sg.WIN_CLOSED:
        layout = [[sg.Text(after_quit)],
                  [sg.Button('yes'), sg.Button('no')]]
        window = sg.Window('rate', layout, margins=(100, 100))
        event, values = window.read()
        if event == 'yes':
            sg.popup(quit_yes_answer)
            window.close()

        elif event == 'no':
            sg.popup(quit_no_answer)
            window.close()

        window.close()


def open_window():
    while True:
        sg.theme('DarkAmber')
        ttk_style = 'vista'
        layout = [[sg.Button('home')],
                  [sg.Button('options')],
                  [sg.Text('welcome to Mood stabilizers')],
                  [sg.Button('lestin to a random song from the library'),
                   sg.Cancel('quit')],
                  [sg.Button('what is my  Mood?')],
                  [sg.Button('Know your mood and let us make you feel better.')],
                  [sg.Button('pick your mood manually')],
                  ]
        window = sg.Window('Mood-Stabilizers', layout,
                           margins=(100, 50), ttk_theme=ttk_style, size=(700, 400))
        event, values = window.read()
        if event == 'lestin to a random song from the library':
            play_sound(random.choice(mood_list))
            window.close()
        elif event == 'what is my  Mood?':
            window.close()
            open_cam()
            break
        elif event == 'Know your mood and let us make you feel better.':
            window.close()
            play_mood()
            break
        elif event == 'pick your mood manually':
            window.close()
            choose_mood()
            break
        elif event == 'home':
            window.close()
            main_page()
        elif event == 'options':
            window.close()
            open_window()
            break
        elif event == 'quit' or event == sg.WIN_CLOSED:
            layout = [[sg.Text(after_quit)],
                      [sg.Button('yes'), sg.Button('no')]]
            window = sg.Window('rate', layout, margins=(100, 100))
            event, values = window.read()
            if event == 'yes':
                sg.popup(quit_yes_answer)
                window.close()
                break
            elif event == 'no':
                sg.popup(quit_no_answer)
                window.close()
                break
    window.close()


def open_cam():
    sg.theme('DarkAmber')
    ttk_style = 'vista'
    layout = [[sg.Button('home')],
              [sg.Button('options')],
              [sg.Text('welcome to mood stabilizers')],
              [sg.Button('what is my currunt Mood?'), sg.Cancel()],
              ]
    window = sg.Window('Mood-Stabilizers', layout,
                       margins=(250, 50), ttk_theme=ttk_style, size=(700, 400))
    event, values = window.read()
    if event == 'what is my currunt Mood?':
        window.close()
        mood = play_cam()
        sg.popup(f'your mood is {mood}')
    elif event == 'home':
        window.close()
        main_page()
    elif event == 'options':
        window.close()
        open_window()
    window.close()


def play_mood():
    while True:
        sg.theme('DarkAmber')
        ttk_style = 'vista'
        layout = [[sg.Button('home')],
                  [sg.Button('options')],
                  [sg.Text('welcome to mood stabilizers')],
                  [sg.Button(
                      'Know your mood and let us make you feel better.'), sg.Cancel()],
                  ]
        window = sg.Window('Mood-Stabilizers', layout,
                           margins=(200, 50), ttk_theme=ttk_style, size=(700, 400))

        event, values = window.read()
        if event == 'Know your mood and let us make you feel better.':
            mood = play_cam()
            if mood:
                close_cam()
                sg.popup(
                    f'your mood is {mood}, we recommend this song for you ')
                play_sound(mood)
                window.close()

                print(1)
        elif event == 'home':
            window.close()
            main_page()
        elif event == 'options':
            window.close()
            open_window()
    window.close()


def choose_mood():
    while True:
        sg.theme('DarkAmber')
        ttk_style = 'vista'
        layout = [
            [sg.Button('home')],
            [sg.Button('options')], [sg.Text('choose a mood')],
            [sg.Button('Angry'), sg.Cancel('quit')],
            [sg.Button('Happy')],
            [sg.Button('Disgusted')],
            [sg.Button('Fearful')],
            [sg.Button('Neutral')],
            [sg.Button('Sad')],
            [sg.Button('Surprised')],
        ]
        window = sg.Window('Mood-Stabilizers', layout,
                           margins=(250, 20), ttk_theme=ttk_style, size=(700, 400))
        event, values = window.read()
        if event in mood_list:
            play_sound(event)
        elif event == 'home':
            window.close()
            main_page()
        elif event == 'options':
            window.close()
            open_window()
        elif event == 'quit' or event == sg.WIN_CLOSED:
            layout = [[sg.Text(after_quit)],
                      [sg.Button('yes'), sg.Button('no')]]
            window = sg.Window('rate', layout, margins=(100, 100))
            event, values = window.read()
            if event == 'yes':
                sg.popup(quit_yes_answer)
                window.close()

                break
            elif event == 'no':
                sg.popup(quit_no_answer)
                window.close()

                break
    window.close()


main_page()
