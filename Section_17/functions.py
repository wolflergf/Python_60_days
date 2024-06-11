FILEPATH = "./todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of do-to items.

    Args:
        filepath (_type_, optional): _description_. Defaults to FILEPATH.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do item list in the text file

    Args:
        todos_arg (list): Write the to-do itms at list.
        filepath (_type_, optional): _description_. Defaults to FILEPATH.
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
