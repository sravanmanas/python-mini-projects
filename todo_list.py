# To-Do List with File Persistence

try :
    with open("tasks.txt","r") as f:
        tasks = f.read().splitlines()
except FileNotFoundError :
    tasks=[]

# Function to display tasks
def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("Your Tasks:")
        i = 1
        for x in tasks:  #can also do, for i,x in enumerate(tasks,1)
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
            task = input("Enter task: ")
            tasks.append(task)
            with open("tasks.txt","a") as f:
             f.write(task + "\n")
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
                        with open("tasks.txt","w") as f:
                            for task in tasks:
                                f.write(task+"\n")                        
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
