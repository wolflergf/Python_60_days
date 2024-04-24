user_prompt = "Enter a todo item: "
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todos)
