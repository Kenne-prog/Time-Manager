from task import Task

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []  # A list to store tasks associated with the user

    def create_task(self, name, description, due_date):
        task = Task(name, description, due_date, self)
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(f"Task: {task.name}, Status: {task.status}")