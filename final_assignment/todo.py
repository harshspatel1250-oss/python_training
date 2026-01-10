'''Create a Python script that implements a simple to-do list manager.
Allow users to add tasks, mark tasks as completed, and remove tasks.
Store the tasks in a list of dictionaries where each dictionary represents a task with keys like 'task_name', 'priority', 'completed', etc.
Provide a menu-driven interface for users to interact with the to-do list.'''


todo_list = []

def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")
    task = {
        "task_name": task_name,
        "priority": priority,
        "completed": False
    }
    todo_list.append(task)
    print("Task added successfully.")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
        return
    print("TASK LIST")
    for i, task in enumerate(todo_list, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['task_name']} | Priority: {task['priority']} | Status: {status}")

def mark_completed():
    view_tasks()
    if not todo_list:
        return
    task_no = int(input("Enter task number to mark as completed: "))
    if 1 <= task_no <= len(todo_list):
        todo_list[task_no - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def remove_task():
    view_tasks()
    if not todo_list:
        return
    task_no = int(input("Enter task number to remove: "))
    if 1 <= task_no <= len(todo_list):
        removed = todo_list.pop(task_no - 1)
        print("Removed task:", removed["task_name"])
    else:
        print("Invalid task number.")

# Menu-driven interface
while True:
    print("\n TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Exiting To-Do List Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
