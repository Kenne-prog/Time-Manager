import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCalendarWidget
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

        calendar_widget = CustomCalendarWidget()
        layout.addWidget(calendar_widget)

        self.events = Events()

    def createEvent(self, title, description, start_date, due_date, estimated_time):
        self.events.createEvent(title, description, start_date, due_date, estimated_time)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
