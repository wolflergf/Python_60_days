while True:
    user_input = input("Enter add, show, complete, edit or exit: ").title().strip()

    if user_input.startswith("Add"):
        todo = user_input[4:]

        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        todo = user_input[4:].title() + "\n"
        todos.append(todo)

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    elif user_input.startswith("Show"):

        with open("./todos.txt", "r") as file:
            todos = file.readlines()

            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo.strip()}")

    elif user_input.startswith("Edit"):
        try:
            number = int(user_input[4:])

            with open("./todos.txt", "r") as file:
                todos = file.readlines()

                todos[number - 1] = input("Enter a new todo: ").title() + "\n"

            with open("./todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_input.startswith("Complete"):
        try:
            number = int(user_input[9:])

            with open("./todos.txt", "r") as file:
                todos = file.readlines()

                todos.pop(number - 1)

            with open("./todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid.")

    elif user_input.startswith("Exit"):
        print("See you soon, bye!")
        break
