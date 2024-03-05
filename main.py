import PySimpleGUI as sg

layout = [
    [sg.Text('Drag and drop directories here:')],
    [sg.Input(size=(50, 1), key='-FOLDER-'), sg.FolderBrowse()],
    [sg.Button('Green',  button_color=('black' ,'#87A920')), sg.Button('Purple', button_color=('white', '#6420AA'))]
]

window = sg.Window('Simple GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Green':
        sg.popup('Green button clicked!')
    elif event == 'Purple':
        sg.popup('Purple button clicked!')

window.close()