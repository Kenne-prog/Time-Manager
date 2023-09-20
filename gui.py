from PyQt5.QtWidgets import QCalendarWidget, QPushButton, QDialog, QListWidget, QTextEdit
from PyQt5.QtCore import Qt, QDate 
from PyQt5.QtGui import QPainter, QFont, QBrush, QTextCharFormat, QColor
from event_creation import EventCreationDialog
from events import Events
from events_window import EventDisplayDialog

class CustomCalendarWidget(QCalendarWidget):
    def __init__(self, events_data):
        super().__init__()

        #Sets the calendars appearance
        self.setGridVisible(False)
        self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        weekend_format = QTextCharFormat()
        weekend_format.setForeground(QBrush(Qt.black, Qt.SolidPattern))
        self.setWeekdayTextFormat(Qt.Saturday, weekend_format)
        self.setWeekdayTextFormat(Qt.Sunday, weekend_format)

        #Creates the button to add events
        self.create_event_button = QPushButton("Create Event")
        self.create_event_button.clicked.connect(self.openEventCreationDialog)
        
        #Adds the button to the calendar
        layout = self.layout()
        layout.addWidget(self.create_event_button)

        #Highlights days
        self.clicked[QDate].connect(self.dayClicked)
        self.selected_date = None


        # Store events data
        self.events_data = events_data

        # Create the event display dialog
        self.event_display_dialog = EventDisplayDialog(self.events_data)


    #Handles the day click
    def dayClicked(self, date):
        if self.selected_date:
            self.setSelectedDate(self.selected_date)
        self.setSelectedDate(date)
        self.selected_date = date

        self.displayEvents(date)


    #edit the cells to make it look nicer
    def paintCell(self, painter, rect, date):
        # Check if the date belongs to the current month and year
        if date.month() == self.monthShown() and date.year() == self.yearShown():
            #Sets the default appearance of each day
            painter.fillRect(rect, Qt.white)
            painter.setPen(Qt.black)
            painter.drawText(rect, Qt.AlignTop | Qt.AlignLeft, str(date.day()))

        #Highlights the day if selected
        if date == self.selected_date:
            highlight_color = QColor(213, 235, 255)
            painter.fillRect(rect, highlight_color)
            painter.setPen(Qt.black)
            painter.drawText(rect, Qt.AlignTop | Qt.AlignLeft, str(date.day()))
            

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

    # Display events for the selected date in the QTextEdit widget
    def displayEvents(self, date):
        self.event_display_dialog.displayEvents(date)
        self.event_display_dialog.show()
