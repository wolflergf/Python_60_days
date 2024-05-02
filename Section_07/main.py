while True:
    user_action = input("Type add, show, edit, complete or exit: ").capitalize().strip()

    match user_action:
        case "Add":
            todo = input("Enter a todo: ") + "\n"

            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("./todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "Show":
            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"{index + 1} - {item.title()}")

        case "Edit":
            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            number = int(input("Number of todo to edit: ")) - 1
            todos[number] = input("Enter a new todo: ") + "\n"

            file = open("./todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "Complete":
            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"{index + 1} - {item.title()}")

            number = int(input("Number of todo completed: ")) - 1
            todos.pop(number)

            file = open("./todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "Exit":
            print("See you!")
            break

        case _:
            print("Something is wrong!")
