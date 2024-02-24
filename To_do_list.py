class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def display_tasks(self):
        for task in self.tasks:
            print(f"{task.title} - {task.status}")

# Example usage:
if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            new_task = Task(title, description, due_date)
            todo_list.add_task(new_task)

        elif choice == "2":
            title_to_remove = input("Enter task title to remove: ")
            todo_list.remove_task(title_to_remove)

        elif choice == "3":
            todo_list.display_tasks()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
