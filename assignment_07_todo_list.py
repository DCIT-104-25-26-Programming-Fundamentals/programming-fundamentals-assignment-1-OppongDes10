
def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 28)
    print("     TO-DO LIST MENU")
    print("=" * 28)
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")
    print("=" * 28)


def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Error: Task cannot be empty.")


def view_tasks(tasks):
    """Display all tasks with numbers."""
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks yet. Your list is empty!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def delete_task(tasks):
    """Delete a task by its number."""
    if not tasks:
        print("Error: No tasks to delete!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f'Task "{deleted_task}" has been removed.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    tasks = []  # List to store all tasks
    print("=== TO-DO LIST APPLICATION STARTED ===\n")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")