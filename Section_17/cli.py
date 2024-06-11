import time

import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's", now)
while True:
    user_input = input("Enter add, show, complete, edit or exit: ").title().strip()

    if user_input.startswith("Add"):
        todo = user_input[4:]

        todos = functions.get_todos()

        todo = user_input[4:].title() + "\n"
        todos.append(todo)

        functions.write_todos(todos)

    elif user_input.startswith("Show"):

        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            print(f"{index + 1} - {todo.strip()}")

    elif user_input.startswith("Edit"):
        try:
            number = int(user_input[4:])

            todos = functions.get_todos()
            todos[number - 1] = input("Enter a new todo: ").title() + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_input.startswith("Complete"):
        try:
            number = int(user_input[9:])

            todos = functions.get_todos()
            todos.pop(number - 1)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_input.startswith("Exit"):
        print("See you soon, bye!")
        break
