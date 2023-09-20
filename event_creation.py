from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QSpinBox, QDateEdit, QMessageBox
from PyQt5.QtCore import Qt, QDate 

#Class from dialog so users can input information of an event
class EventCreationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Event")

        #All the elements that make an event
        self.title_label = QLabel("Event Title:")
        self.title_edit = QLineEdit()

        self.description_label = QLabel("Event Description:")
        self.description_edit = QLineEdit()

        self.time_unit_label = QLabel("Time Unit:")
        self.time_unit_combo = QComboBox()
        self.time_unit_combo.addItems(["Days", "Hours"])

        self.time_duration_label = QLabel("Estimated Time til Completion:")
        self.time_duration_spinbox = QSpinBox()
        self.time_duration_spinbox.setMinimum(1) 

        self.start_date_label = QLabel("Start Date:")
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setDate(QDate.currentDate())  # Set the default date to the current date

        self.end_date_label = QLabel("End Date:")
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setDate(QDate.currentDate())

        # Adds the widgets to the boxlayot

        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_edit)

        layout.addWidget(self.description_label)
        layout.addWidget(self.description_edit)

        layout.addWidget(self.time_unit_label)
        layout.addWidget(self.time_unit_combo)

        layout.addWidget(self.time_duration_label)
        layout.addWidget(self.time_duration_spinbox)

        layout.addWidget(self.start_date_label)
        layout.addWidget(self.start_date_edit)

        layout.addWidget(self.end_date_label)
        layout.addWidget(self.end_date_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept_dialog)

    #methods to get the elements
    def get_title(self):
        return self.title_edit.text()

    def get_description(self):
        return self.description_edit.text()

    def get_time_unit(self):
        return self.time_unit_combo.currentText()

    def get_time_duration(self):
        return self.time_duration_spinbox.value()

    def get_start_date(self):
        return self.start_date_edit.date()

    def get_end_date(self):
        return self.end_date_edit.date()


    def accept_dialog(self):
        # Validate the end date to ensure it's on or after the start date
        start_date = self.get_start_date()
        end_date = self.get_end_date()

        if start_date > end_date:
            QMessageBox.critical(self, "Invalid Date", "End date must be on or after the start date.")
            return

        # If validation passes, accept the dialog
        self.accept()

    