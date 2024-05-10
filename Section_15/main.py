from functions import get_todos, write_todos


while True:
    user_input = input("Enter add, show, complete, edit or exit: ").title().strip()

    if user_input.startswith("Add"):
        todo = user_input[4:]

        todos = get_todos()

        todo = user_input[4:].title() + "\n"
        todos.append(todo)

        write_todos(todos)

    elif user_input.startswith("Show"):

        todos = get_todos()

        for index, todo in enumerate(todos):
            print(f"{index + 1} - {todo.strip()}")

    elif user_input.startswith("Edit"):
        try:
            number = int(user_input[4:])

            todos = get_todos()
            todos[number - 1] = input("Enter a new todo: ").title() + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_input.startswith("Complete"):
        try:
            number = int(user_input[9:])

            todos = get_todos()
            todos.pop(number - 1)

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_input.startswith("Exit"):
        print("See you soon, bye!")
        break
