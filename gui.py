import tkinter as tk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Create UI elements and set up the GUI
        # ...
        self.count_label = tk.Label(root, text="Count: 0")
        self.count_label.pack()
        
        count = 0
        # Create a button
        self.button = tk.Button(root, text="Click Me", command=self.increment_count)
        self.button.pack()  # Place the button in the window using pack()
        self.count = 0

    def increment_count(self):
        # Increment the count and update the label text
        self.count += 1
        self.count_label.config(text=f"Count: {self.count}")