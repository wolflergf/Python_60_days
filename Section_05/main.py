todos = []

while True:
    user_action = input("Tipe add, show, edit or exit: ").capitalize().strip()

    match user_action:
        case "Add":
            todo = input("Add a new todo: ")
            todos.append(todo)
        case "Show":
            for item in todos:
                print(item.title())
        case "Exit":
            print("Goodbye!")
            break
        case "Edit":
            for index, item in enumerate(todos):
                print(index + 1, "-", item.title())
            index = int(input("Type the index of the todo you want to edit: ")) - 1
            new_todo = input("Type the new todo: ")
            todos[index] = new_todo
        case _:
            print("Invalid action")
