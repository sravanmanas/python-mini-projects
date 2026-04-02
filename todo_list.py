# Simple CLI To-Do List Application

tasks = []

# Function to display tasks
def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("Your Tasks:")
        i = 1
        for x in tasks:  #can also do, for i,x in enumerate(task,1)
            print(i, x)
            i += 1
        print()


def menu():
    while True:
        n = input(
            "1. Add Task\n"
            "2. View Tasks\n"
            "3. Delete Task\n"
            "4. Exit\n"
            "Enter your choice: "
        )

        # Add Task
        if n == "1":
            tasks.append(input("Enter task: "))
            print("Task added successfully.\n")

        # View Tasks
        elif n == "2":
            view_tasks()

        # Delete Task
        elif n == "3":
            if not tasks:
                print("No tasks available to delete.\n")
            else:
                view_tasks()
                try:
                    delete = int(input("Enter task number to delete: "))
                    if 1 <= delete <= len(tasks):
                        del tasks[delete - 1]
                        print("Task deleted successfully.\n")
                    else:
                        print("Invalid task number.\n")
                except ValueError:
                    print("Please enter a valid number.\n")

        # Exit
        elif n == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


# Start program
menu()
