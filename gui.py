import tkinter as tk
import calendar

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(screen_width * 0.5)}x{int(screen_height * 0.5)}+{(screen_width - int(screen_width * 0.5)) // 2}+{(screen_height - int(screen_height * 0.5)) // 2}")

        
        # Create a frame to hold the calendar
        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack(fill=tk.BOTH, expand=True)  # Fill and expand with the window

        # Create a calendar object for the current month
        self.cal = calendar.monthcalendar(2023, 1)  # Replace with the desired year and month

        # Create a grid of labels to represent each day
        for row, week in enumerate(self.cal):
            for col, day in enumerate(week):
                if day == 0:
                    continue
                label = tk.Label(self.calendar_frame, text=str(day),anchor = "nw", padx=10, pady=10, borderwidth=1, relief="solid")
                label.grid(row=row, column=col, sticky="nsew")  # Sticky makes labels expand with the grid cell

        # Configure row and column weights for the calendar frame
        for i in range(7):  # Assuming 7 columns for the days of the week
            self.calendar_frame.columnconfigure(i, weight=1)
        for i in range(len(self.cal) + 1):  # Adjust for the number of rows in the calendar
            self.calendar_frame.rowconfigure(i, weight=1)