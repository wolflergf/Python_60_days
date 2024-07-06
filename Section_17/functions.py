import os
from datetime import datetime

FILEPATH = "./todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip().split("|") for line in file.readlines()]


def write_todos(todos, filepath=FILEPATH):
    """Write the to-do item list to the text file."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(f"{item[0]}|{item[1]}|{item[2]}\n" for item in todos)


def add_todo(todos, new_todo):
    """Add a new to-do item to the list."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    todos.append([new_todo.capitalize(), current_date, "Pending"])
    write_todos(todos)


def update_todo_status(todos, index, new_status):
    """Update the status of a to-do item."""
    todos[index][2] = new_status
    write_todos(todos)


def delete_todo(todos, index):
    """Delete a to-do item from the list."""
    todos.pop(index)
    write_todos(todos)


if __name__ == "__main__":
    print("Current todos:", get_todos())
