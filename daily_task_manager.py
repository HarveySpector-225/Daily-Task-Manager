# Daily Task Manager (PS 28) - tasks are saved in tasks.txt as id|title|priority|due_date|status
from datetime import datetime

FILE = "tasks.txt"


def load_tasks():
    tasks = []
    try:
        f = open(FILE, "r")
        for line in f.read().split("\n"):
            p = line.strip().split("|")
            if len(p) == 5:
                tasks.append({"id": p[0], "title": p[1], "priority": p[2],
                              "due_date": p[3], "status": p[4]})
        f.close()
    except FileNotFoundError:
        pass  # first run: no file yet
    return tasks


def save_tasks(tasks):
    f = open(FILE, "w")
    for t in tasks:
        f.write("|".join([t["id"], t["title"], t["priority"], t["due_date"], t["status"]]) + "\n")
    f.close()


def is_valid_date(text):
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return len(text) == 10  # rejects things like 2026-1-5
    except ValueError:
        return False


def get_next_task_id(tasks):
    biggest = 100
    for t in tasks:
        if int(t["id"][1:]) > biggest:
            biggest = int(t["id"][1:])
    return "T" + str(biggest + 1)


def count_pending(tasks):
    count = 0
    for t in tasks:
        if t["status"] == "Pending":
            count += 1
    return count


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title == "" or "|" in title:
        print("Title cannot be empty or contain the | symbol.")
        return
    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority. Enter High, Medium or Low.")
        return
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    if not is_valid_date(due_date):
        print("Invalid date. Use YYYY-MM-DD.")
        return
    task = {"id": get_next_task_id(tasks), "title": title, "priority": priority,
            "due_date": due_date, "status": "Pending"}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")
    print(" | ".join([task["id"], title, priority, due_date, "Pending"]))


def view_by_priority(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    for level in ["High", "Medium", "Low"]:
        for t in tasks:
            if t["priority"] == level:
                print(" | ".join([t["id"], t["title"], t["priority"], t["due_date"]]))


def show_pending(tasks):
    pending = count_pending(tasks)
    if pending == 0:
        print("No pending tasks. You are all caught up!")
        return
    for t in tasks:
        if t["status"] == "Pending":
            print(" | ".join([t["id"], t["title"], t["priority"], t["due_date"]]))
    print("Total pending tasks:", pending)


def complete_task(tasks):
    task_id = input("Enter task ID: ").strip().upper()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "Done"
            save_tasks(tasks)
            print("Task " + task_id + " marked as done. Pending tasks:", count_pending(tasks))
            return
    print("Task " + task_id + " not found.")


def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add task\n2. View by priority\n3. Show pending\n4. Complete task\n5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_by_priority(tasks)
        elif choice == "3":
            show_pending(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Enter a number from 1 to 5.")


main()
