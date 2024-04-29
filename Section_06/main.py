todos = []

while True:
    user_action = input("Type add, show, edit, remove or exit: ").capitalize().strip()

    match user_action:
        case "Add":
            todo = input("Enter a todo: ").title()
            todos.append(todo)

        case "Show":
            for index, item in enumerate(todos):
                print(index + 1, "-", item)

        case "Edit":
            for index, item in enumerate(todos):
                print(index + 1, "-", item)

            index = int(input("Number of the todo to edit: ")) - 1
            new_todo = input("Enter new todo: ").title()
            todos[index] = new_todo

        case "Remove":
            for index, item in enumerate(todos):
                print(index + 1, "-", item)

            index = int(input("Number of the todo to remove: ")) - 1
            todos.pop(index)

        case "Exit":
            print("See you later!")
            break

        case _:
            print("There are something wrong!")
