import time

import FreeSimpleGUI as sg

import functions

sg.theme("Black")
layout = [
    [sg.Text("", key="real_time")],
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
    [
        sg.Button("Edit", key="edit"),
        sg.Button("Complete", key="complete"),
        sg.Button("Exit", key="exit"),
    ],
]

window = sg.Window("My To-Do App", layout)


while True:
    event, values = window.read(timeout=200)
    window["real_time"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Select a item first.")

        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")

            except IndexError:
                sg.popup("Select a item first.")

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "exit":
            break

        case sg.WIN_CLOSED:
            break
window.close()
