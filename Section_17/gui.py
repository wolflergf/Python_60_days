import FreeSimpleGUI as sg

import functions

layout = [
    [sg.Text("Type in a to-do")],
    [
        sg.InputText(tooltip="Enter to-do", key="todo"),
        sg.Button("Add", key="add"),
    ],
]

# label = sg.Text("Type in a to-do")
# input_box = sg.InputText(tooltip="Enter todo")
# add_button = sg.Button("Add")
# window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])

window = sg.Window("My To-Do App", layout)


while True:

    event, values = window.read()
    if event == "add":
        todos = functions.get_todos()
        todos.append(values["todo"] + "\n")
        functions.write_todos(todos)
    elif sg.WIN_CLOSED:
        break

    print(event, values)
window.close()
