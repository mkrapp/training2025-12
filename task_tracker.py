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

def main():
    print("Simple Task Tracker")
    print("Options: add, list, done")
    choice = input("What do you want to do? ")

    tasks = load_tasks()

    if choice == "list":
        for t in tasks:
            print("-", t)

if __name__ == "__main__":
    main()
