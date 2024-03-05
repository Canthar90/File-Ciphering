import PySimpleGUI as sg
from file_cyphering import EncryptFiles
import os

encrypter = EncryptFiles()

layout = [
    [sg.Text('Drag and drop directories here:')],
    [sg.Input(size=(50, 1), key='-PATH-', enable_events=True), sg.FolderBrowse()],
    [sg.Button('Green',  button_color=('black' ,'#87A920')), sg.Button('Purple', button_color=('white', '#6420AA'))]
]

window = sg.Window('Simple GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Green':
        sg.popup('Green button clicked!')
        path = values['-PATH-']
        print(path)
    elif event == 'Purple':
        sg.popup('Purple button clicked!')

window.close()