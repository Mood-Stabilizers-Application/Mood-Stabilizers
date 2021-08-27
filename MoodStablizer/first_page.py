import PySimpleGUI as sg
from sound.sound import play_sound
import random
from CamDetect import play_cam, close_cam
mood_list = ['Angry', 'Disgusted', 'Fearful',
             'Happy', 'Neutral', 'Sad', 'Surprised']
after_quit = 'Did you like your experience with Mood Stabilizer App?'
quit_yes_answer = 'Thank you!'
quit_no_answer = 'Sorry to hear that!'


def main_page():
    sg.theme('DarkAmber')
    ttk_style = 'vista'
    layout = [[sg.Text('Mood-Stabilizers-App')],
              [sg.Button('Start'), sg.Cancel('Quit')]]
    window = sg.Window('Mood-Stabilizers-App', layout,
                       margins=(250, 150), ttk_theme=ttk_style, size=(700, 400))
    event, values = window.read()
    print(values)
    print(event)
    if event == 'Start':
        # pass
        window.close()
        open_window()
    elif event == 'Quit' or event == sg.WIN_CLOSED:
        layout = [[sg.Text(after_quit)],
                  [sg.Button('Yes'), sg.Button('No')]]
        window = sg.Window('rate', layout, margins=(100, 100))
        event, values = window.read()
        if event == 'Yes':
            sg.popup(quit_yes_answer)
            window.close()

        elif event == 'No':
            sg.popup(quit_no_answer)
            window.close()

        window.close()


def open_window():
    while True:
        sg.theme('DarkAmber')
        ttk_style = 'vista'
        layout = [[sg.Button('Home')],
                  [sg.Button('Options')],
                  [sg.Text('Welcome to Mood Stabilizers App!')],
                  [sg.Button('Listen to random song from the library!'),
                   sg.Cancel('Quit')],
                  [sg.Button('What is my Mood?')],
                  [sg.Button('Know your mood and let us make you feel better!')],
                  [sg.Button('Pick your mood manually!')],
                  ]
        window = sg.Window('Mood-Stabilizers-App', layout,
                           margins=(100, 50), ttk_theme=ttk_style, size=(700, 400))
        event, values = window.read()
        if event == 'Listen to random song from the library!':
            play_sound(random.choice(mood_list))
            window.close()
        elif event == 'What is my Mood?':
            window.close()
            open_cam()
            break
        elif event == 'Know your mood and let us make you feel better!':
            window.close()
            play_mood()
            break
        elif event == 'Pick your mood manually!':
            window.close()
            choose_mood()
            break
        elif event == 'Home':
            window.close()
            main_page()
        elif event == 'Options':
            window.close()
            open_window()
            break
        elif event == 'Quit' or event == sg.WIN_CLOSED:
            layout = [[sg.Text(after_quit)],
                      [sg.Button('Yes'), sg.Button('No')]]
            window = sg.Window('rate', layout, margins=(100, 100))
            event, values = window.read()
            if event == 'Yes':
                sg.popup(quit_yes_answer)
                window.close()
                break
            elif event == 'No':
                sg.popup(quit_no_answer)
                window.close()
                break
    window.close()


def open_cam():
    sg.theme('DarkAmber')
    ttk_style = 'vista'
    layout = [[sg.Button('Home')],
              [sg.Button('Options')],
              [sg.Text('Welcome to Mood Stabilizers App!')],
              [sg.Button('What is my current mood?'), sg.Cancel()],
              ]
    window = sg.Window('Mood-Stabilizers-App', layout,
                       margins=(250, 50), ttk_theme=ttk_style, size=(700, 400))
    event, values = window.read()
    if event == 'What is my current mood?':
        window.close()
        mood = play_cam()
        sg.popup(f'Your mood is {mood}')
        open_cam()
    elif event == 'Home':
        window.close()
        main_page()
    elif event == 'Options':
        window.close()
        open_window()
    window.close()


def play_mood():
    sg.theme('DarkAmber')
    ttk_style = 'vista'
    layout = [[sg.Button('Home')],
                [sg.Button('Options')],
                [sg.Text('Welcome to Mood Stabilizers App!')],
                [sg.Button(
                    'Know your mood and let us make you feel better!'), sg.Cancel()],
                ]
    window = sg.Window('Mood-Stabilizers-App', layout,
                        margins=(200, 50), ttk_theme=ttk_style, size=(700, 400))

    event, values = window.read()
    if event == 'Know your mood and let us make you feel better!':
        mood = play_cam()
        if mood:
            sg.popup(
                f'Your mood is {mood}, We recommend this song for you!')
            play_sound(mood)
            play_mood()
    elif event == 'Home':
        window.close()
        main_page()
    elif event == 'Options':
        window.close()
        open_window()
    window.close()


def choose_mood():
    sg.theme('DarkAmber')
    ttk_style = 'vista'
    layout = [
        [sg.Button('Home')],
        [sg.Button('Options')], [sg.Text('Choose mood!')],
        [sg.Button('Angry'), sg.Cancel('Quit')],
        [sg.Button('Happy')],
        [sg.Button('Disgusted')],
        [sg.Button('Fearful')],
        [sg.Button('Neutral')],
        [sg.Button('Sad')],
        [sg.Button('Surprised')],
    ]
    window = sg.Window('Mood-Stabilizers-App', layout,
                        margins=(250, 20), ttk_theme=ttk_style, size=(700, 400))
    event, values = window.read()
    if event in mood_list:
        play_sound(event)
        choose_mood()
    elif event == 'Home':
        window.close()
        main_page()
    elif event == 'Options':
        window.close()
        open_window()
    elif event == 'Quit' or event == sg.WIN_CLOSED:
        layout = [[sg.Text(after_quit)],
                    [sg.Button('Yes'), sg.Button('No')]]
        window = sg.Window('rate', layout, margins=(100, 100))
        event, values = window.read()
        if event == 'Yes':
            sg.popup(quit_yes_answer)
            window.close()

        elif event == 'No':
            sg.popup(quit_no_answer)
            window.close()

    window.close()


main_page()
