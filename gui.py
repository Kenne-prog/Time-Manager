from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPainter, QFont

class CustomCalendarWidget(QCalendarWidget):
    def __init__(self):
        super().__init__()

        # Set the font and alignment for day numbers
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)

        # Set the gridVisible property to False to hide days from other months
        self.setGridVisible(False)

    def paintCell(self, painter, rect, date):
        # Check if the date belongs to the current month and year
        if date.month() == self.monthShown() and date.year() == self.yearShown():
            # Fill the cell with a white background
            painter.fillRect(rect, Qt.white)
            
            # Set the text color to black
            painter.setPen(Qt.black)
            
            # Draw the custom day number in the top-left corner
            painter.drawText(rect, Qt.AlignTop | Qt.AlignLeft, str(date.day()))
