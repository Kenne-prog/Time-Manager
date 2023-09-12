class Task:
    def __init__(self, name, description, due_date, owner):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"
        self.owner = owner

    def mark_complete(self):
        self.status = "Complete"

    def edit_task(self, new_name, new_description, new_due_date):
        self.name = new_name
        self.description = new_description
        self.due_date = new_due_date