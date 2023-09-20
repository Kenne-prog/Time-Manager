from PyQt5.QtWidgets import QCalendarWidget, QPushButton, QVBoxLayout, QTextEdit, QWidget, QDialog
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPainter, QTextCharFormat, QBrush, QColor

class EventDisplayDialog(QDialog):
    def __init__(self, events_data):
        super().__init__()

        self.setWindowTitle("Event Display")
        self.setMinimumSize(400, 300)

        self.event_display = QTextEdit()
        self.event_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.event_display)
        self.setLayout(layout)

        self.events_data = events_data

    def displayEvents(self, date):
        events_for_date = self.events_data.get(date, [])
        event_text = "\n".join(events_for_date)
        self.event_display.setPlainText(event_text)