"""A simple command-line To-Do list manager using JSON."""
import argparse
import json
from pathlib import Path

TODO_FILE = Path(__file__).with_name("todos.json")

def load_todos():
    if TODO_FILE.exists():
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="The task description")
    
    subparsers.add_parser("list", help="List all tasks")
    
    done_parser = subparsers.add_parser("done", help="Mark a task as completed")
    done_parser.add_argument("id", type=int, help="The task ID to mark done")
    
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="The task ID to delete")

    args = parser.parse_args()
    
    # Handle the case where no command is provided
    if not hasattr(args, 'command') or args.command is None:
        parser.print_help()
        return

    todos = load_todos()

    if args.command == "add":
        todos.append({"task": args.task, "done": False})
        save_todos(todos)
        print("Task added.")
    elif args.command == "list":
        if not todos:
            print("No tasks found.")
        else:
            for i, todo in enumerate(todos, 1):
                status = "[x]" if todo["done"] else "[ ]"
                print(f"{i}. {status} {todo['task']}")
    elif args.command == "done":
        if 1 <= args.id <= len(todos):
            todos[args.id - 1]["done"] = True
            save_todos(todos)
            print("Task marked as done.")
        else:
            print("Invalid task ID.")
    elif args.command == "delete":
        if 1 <= args.id <= len(todos):
            deleted = todos.pop(args.id - 1)
            save_todos(todos)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task ID.")

if __name__ == "__main__":
    main()
