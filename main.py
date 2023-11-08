import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import Qt, QDate 
from gui import CustomCalendarWidget
from events import Events
from event_creation import EventCreationDialog


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Time Manager")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        events_data = {}

        calendar_widget = CustomCalendarWidget(events_data)
        layout.addWidget(calendar_widget)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
