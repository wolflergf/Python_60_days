todos = []

while True:
    user_action = input("Type add, show or exit: ").capitalize().strip()

    match user_action:
        case "Add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "Show":
            for todo in todos:
                print(todo)
        case "Exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid action")
