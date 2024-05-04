while True:
    user_action = input("Type add, show, edit, complete or exit: ").title()

    match user_action:
        case "Add":
            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            todo = input("Enter a todo: ").title()
            todos.append(f"{todo}\n")

            file = open("./todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "Show":
            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            # List comprehension
            # todos = [item.strip("\n" for todo in todos)]

            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo.strip()}")

        case "Edit":

            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo.strip()}")

            number_to_edit = int(input("Enter the number to edit: ")) - 1
            todos[number_to_edit] = input("Enter a new todo: ").title() + "\n"

            file = open("./todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "Complete":

            file = open("./todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo.strip()}")

            number_to_edit = int(input("Enter the number to edit: ")) - 1
            todos.pop(number_to_edit)

            file = open("./todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "Exit":
            print("See you soon!")
            break

        case _:
            print("Something is wrong!")
