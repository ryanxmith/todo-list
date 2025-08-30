import json


def main():
    tasks = []

    # Options menu
    while True:
        print("\n--- To-Do-List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Complete task")
        print("5. Quit")

        # User input
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Displays all the tasks


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['name']} [{status}]")

# Adds a new task


def add_task(tasks):
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print(f"Task '{name}' added.")

# Marks the task as complete


def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter task number to complete: ")) - 1
            tasks[choice]["done"] = True
            print(f"Task '{tasks[choice]['name']}' marked complete.")
        except (ValueError, IndexError):
            print("Invalid task number.")

# Deletes a task


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(choice)
        print(f"Task '{removed['name']}' deleted.")
    except:
        print("Invalid task number.")

# Loads tasks from a json file


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Saves tasks to a json file


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


if __name__ == "__main__":
    main()
