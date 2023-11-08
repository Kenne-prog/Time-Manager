from PyQt5.QtWidgets import QCalendarWidget, QVBoxLayout, QTextEdit, QWidget, QDialog, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor

class EventDisplayDialog(QDialog):
    def __init__(self, events_data):
        super().__init__()

        self.setWindowTitle("Event Display")
        self.setMinimumSize(400, 300)

        self.event_list = QListWidget()
        self.event_list.itemClicked.connect(self.handleEventClick)

        layout = QVBoxLayout()
        layout.addWidget(self.event_list)
        self.setLayout(layout)

        self.events_data = events_data

    def displayEvents(self, date):
        events_for_date = self.events_data.get(date, [])

        for event in events_for_date:
            print(event)
            item = QListWidgetItem(event)
            item.setData(Qt.UserRole, event)  # Store the event text as item data
            self.event_list.addItem(item)

    def handleEventClick(self, item):
        # Retrieve the event text from the clicked item's data
        event_text = item.data(Qt.UserRole)
        if event_text:
            self.showEventDetails(event_text)

    def showEventDetails(self, event_text):
        # You can implement how you want to show the event details here
        # For example, open a new window or display a dialog
        pass
