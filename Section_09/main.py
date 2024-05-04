while True:
    user_action = input("Type add, show, edit, complete or exit: ").title().strip()

    match user_action:
        case "Add":
            todo = input("Enter a todo: ").title() + "\n"

            with open("./todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("./todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

        case "Show":
            with open("./todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()

                for index, todo in enumerate(todos):
                    print(f"{index + 1} - {todo.strip()}")

        case "Edit":
            with open("./todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()

            number = int(input("Number of the todo for edit: ")) - 1
            todos[number] = input("Enter a new todo: ").title() + "\n"

            with open("./todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

        case "Complete":
            with open("./todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()

            number = int(input("Number of the todo for delete: ")) - 1
            print(f"Todo '{todos[number].strip()}' was removed form the list.")
            todos.pop(number)

            with open("./todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

        case "Exit":
            print("See you soon!")
            break

        case _:
            print("There are something wrong. Tray again!")
