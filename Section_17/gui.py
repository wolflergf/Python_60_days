import FreeSimpleGUI as sg

import functions

layout = [
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter to-do"), sg.Button("Add")],
]

# label = sg.Text("Type in a to-do")
# input_box = sg.InputText(tooltip="Enter todo")
# add_button = sg.Button("Add")
# window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])

window = sg.Window("My To-Do App", layout)
window.read()
window.close()
