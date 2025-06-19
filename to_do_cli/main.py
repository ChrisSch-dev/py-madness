import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)

def list_todos():
    todos = load_todos()
    for i, todo in enumerate(todos, 1):
        status = "[x]" if todo["done"] else "[ ]"
        print(f"{i}. {status} {todo['task']}")

def complete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        save_todos(todos)

def remove_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos.pop(index)
        save_todos(todos)

def main():
    print("To-Do CLI App. Commands: add, list, done, remove, quit")
    while True:
        cmd = input("> ").strip().split(maxsplit=1)
        if not cmd:
            continue
        action = cmd[0]
        arg = cmd[1] if len(cmd) > 1 else None
        if action == "add" and arg:
            add_todo(arg)
        elif action == "list":
            list_todos()
        elif action == "done" and arg and arg.isdigit():
            complete_todo(int(arg)-1)
        elif action == "remove" and arg and arg.isdigit():
            remove_todo(int(arg)-1)
        elif action == "quit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()