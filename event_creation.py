from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

#Class from dialog so users can input information of an event
class EventCreationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Event")

        self.title_label = QLabel("Event Title:")
        self.title_edit = QLineEdit()

        # Add other input fields for event details (description, start date, due date, estimated time)

        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_edit)
        # Add other input fields to the layout

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def get_title(self):
        return self.title_edit.text()

    # Implement similar methods for other input fields (description, dates, estimated time)
