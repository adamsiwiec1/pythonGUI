# Normal GUI
# import PySimpleGUI as sg
# Cute GUI - nicer buttons?
import PySimpleGUIQt as sg
# Wide GUI - similar to Qt
# import PySimpleGUIWx as sg - didnt work
# Web Browser GUI
# import PySimpleGUIWeb as sg - didnt work - both had package error

# Define the window's contents

layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]


# Create the window object
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
