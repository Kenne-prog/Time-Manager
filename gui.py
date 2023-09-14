import tkinter as tk
from tkcalendar import Calendar

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")


        # Create the calendar widget with expanded options
        cal = Calendar(self.root, selectmode='day', year=2023, month=1, day=1, showothermonthdays=False, showweeknumbers=False,weekendbackground = "white")
        
        
        cal.pack(fill='both', expand=True, padx=10, pady=10)  # Use fill and expand options

        

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
