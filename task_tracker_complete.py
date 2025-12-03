TASK_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for i, task in enumerate(tasks):
        print(i, "-", task)


def add_task(tasks):
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added.")


def complete_task(tasks):
    if not tasks:
        print("No tasks to complete.")
        return

    list_tasks(tasks)

    try:
        index = int(input("Which task is done? "))
        finished = tasks.pop(index)
        save_tasks(tasks)
        print("Completed:", finished)
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    print("\n--- Simple Task Tracker ---")
    print("1 - Add task")
    print("2 - List tasks")
    print("3 - Mark task as done")

    choice = input("Choose an option: ")

    tasks = load_tasks()

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        list_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    else:
        print("Unknown option.")


if __name__ == "__main__":
    main()
