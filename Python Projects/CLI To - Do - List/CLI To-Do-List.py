tasks = []
titles = set()

def show_menu():
    print("1. Add Task ")
    print("2. View Task")
    print("3. Mark As Done")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

def add_task():
    title = input("Enter Task Title: ").strip().lower()
    priority = input("Enter Priority (High/Low): ").lower()

    if priority not in ["high", "low"]:
        print("Invalid priority! Setting to low by default.")
        priority = "low"

    if title in titles:
        print("Task already Exist!")
    else:
        new_task = {
            "title" : title,
            "status" : "pending",
            "priority" : priority
        }

        tasks.append(new_task)
        titles.add(title)
        line()
        print(f"Task '{title}' added successfully!, status is {new_task['status']}")
        line()

def view_task():
    if not tasks:
        print("There is No tasks!")
        return
    
    display_tasks()

def mark_as_done():
    if not tasks:
        print("Your Tasks list is Empty")
        return

    display_tasks()

    try:
        task_num = int(input("Enter the task number: "))
        index = task_num - 1

        if 0 <= index < len(tasks):
            tasks[index]["status"] = "done"
            line()
            print(f"Task '{tasks[index]['title']}' marked as done!")
            line()
        else:
            print("Invalid number..!")
    except(ValueError):
        print("There is no task with the given number please enter a valid number..!")
       
def delete_task():
    if not tasks:
        print("Your Tasks list is Empty")
        return
    
    display_tasks()
    
    try:
        index = int(input("Enter the task number to delete: "))
        index -= 1

        if 0 <= index < len(tasks):
            confirm = input("Are you sure ? (y/n): ")
            if confirm.lower() == "y":
                removed_task = tasks.pop(index)
                titles.remove(removed_task["title"])
                line()
                print(f"Successfully Deleted")
                line()
                print("Your Remaining tasks")
                view_task()
            else:
                print("Deletion Cancelled.")
        else:
            print("Invalid number..!")

    except ValueError:
        print("Enter valid Number...!")

def search_task():

    if not tasks:
        print("There is no tasks available!")
        return
    keyword = input("Enter task name for searching: ").strip()
    found = False
    for task in tasks:
        if keyword.lower() in task["title"].lower():
            print(f"The task {task['title']} is available!")
            found = True
    if not found:
        print("No matching task found!")

def exit_program():
    print("Exiting The Program...!")
    return

def line():
    print("=" * 40)

def display_tasks():
    line()
    print("---------Current Tasks---------")
    print("No | Title | Status | Priority")
    for i, task in enumerate(tasks, start=1):
        print(f"{i:<3} | {task['title']:<15} | {task['status']:<8} | {task['priority']}")
    line()
    
while True:
    show_menu()

    choice = input("Enter Your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_as_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        search_task()
    elif choice == "6":
        exit_program()
        break
    else:
        print("Enter a valid number..!")