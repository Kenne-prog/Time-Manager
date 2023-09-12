import tkinter as tk
from task import Task
from user import User
from gui import TaskManagerApp

def main():
    root = tk.Tk()  # Create the main application window
    app = TaskManagerApp(root)  # Initialize your Task Manager App within the window
    root.mainloop()  # Start the Tkinter main event loop

if __name__ == "__main__":
    main()  # Call the main function to run your application
