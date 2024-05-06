while True:
    user_action = input("Type add, show, complete, edit or exit: ").title().strip()

    if user_action == "Add":
        todo = input("Enter a todo: ").title()

        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "Show":
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            print(f"{index + 1} - {todo.strip()}")

    elif user_action == "Complete":
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        number = int(input("Enter the number to delete: ")) - 1
        todos.pop(number)

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "Edit":
        with open("./todos.txt", "r") as file:
            todos = file.readlines()

        number = int(input("Enter the number to edit: ")) - 1
        new_todo = input("Enter a new todo: ").title()
        todos[number] = new_todo + "\n"

        with open("./todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "Exit":
        print("See you soon!")
        break

    else:
        print("Somethong is Wrong!")
