from PyQt5.QtWidgets import QCalendarWidget, QPushButton, QDialog
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPainter, QFont, QBrush, QTextCharFormat
from event_creation import EventCreationDialog
from events import Events

class CustomCalendarWidget(QCalendarWidget):
    def __init__(self):
        super().__init__()

        # Set the font and alignment for day numbers

        # Set the gridVisible property to False to hide days from other months
        self.setGridVisible(False)

        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        weekend_format = QTextCharFormat()
        weekend_format.setForeground(QBrush(Qt.black, Qt.SolidPattern))  # Set text color to black

        # Set the format for Saturday and Sunday in the calendar widget
        self.setWeekdayTextFormat(Qt.Saturday, weekend_format)
        self.setWeekdayTextFormat(Qt.Sunday, weekend_format)

        #Creates the button to add events
        self.create_event_button = QPushButton("Create Event")
        self.create_event_button.clicked.connect(self.openEventCreationDialog)
        
        #Adds the button to the calendar
        layout = self.layout()
        layout.addWidget(self.create_event_button)


    #edit the cells to make it look nicer
    def paintCell(self, painter, rect, date):
        # Check if the date belongs to the current month and year
        if date.month() == self.monthShown() and date.year() == self.yearShown():
            # Fill the cell with a white background
            painter.fillRect(rect, Qt.white)
            
            painter.setPen(Qt.black)
            calendarWidget = QCalendarWidget()
            
            # Draw the custom day number in the top-left corner
            painter.drawText(rect, Qt.AlignTop | Qt.AlignLeft, str(date.day()))
            self.button = QPushButton("+", self)
            self.button.setGeometry(5,5,5,5)  # Set the button's geometry to cover the entire cell
            self.button.clicked.connect(lambda _, date=date: self.openEventCreationDialog(date))
            

    # opens the dialog box so users can enter information for events
    def openEventCreationDialog(self):
        dialog = EventCreationDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            # Handle event creation here (e.g., pass user inputs to createEvent method)
            title = dialog.get_title()
            description = dialog.get_description()
            start_date = dialog.get_start_date()
            due_date = dialog.get_due_date()
            estimated_time = dialog.get_estimated_time()
            self.createEvent(title, description, start_date, due_date, estimated_time)