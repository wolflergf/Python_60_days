import streamlit as st

import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo.capitalize())
    functions.write_todos(todos)


st.title("To-do App")


for todo in todos:
    st.checkbox(todo, key=todo)


st.text_input(
    label="Enter a todo",
    label_visibility="hidden",
    placeholder="Add a to-do...",
    on_change=add_todo,
    key="new_todo",
)

print("hello")

st.session_state
