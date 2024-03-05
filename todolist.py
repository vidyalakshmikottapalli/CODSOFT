class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("Your to-do list is empty.")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
