import FreeSimpleGUI as sg

import functions

layout = [
    [sg.Text("Type in a to-do")],
    [
        sg.InputText(tooltip="Enter to-do", key="todo"),
        sg.Button("Add", key="add"),
    ],
    [
        sg.Listbox(
            values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]
        )
    ],
    [sg.Button("Edit", key="edit")],
]

# label = sg.Text("Type in a to-do")
# input_box = sg.InputText(tooltip="Enter todo")
# add_button = sg.Button("Add")
# window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])

window = sg.Window("My To-Do App", layout)


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break
window.close()
