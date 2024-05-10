def get_todos(filepath="./todos.txt"):
    """Read a text file and return a list of to-do items.

    Args:
        filepath (str, optional): Read a text file. Defaults to "./todos.txt".

    Returns:
        List: list of to-do item.
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="./todos.txt"):
    """Write the to-do items list in the text file

    Args:
        todos_arg (list): Write the to-do items
        filepath (str, optional): Text file. Defaults to "./todos.txt".
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
