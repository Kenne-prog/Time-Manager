from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPainter, QFont, QBrush, QTextCharFormat

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

    def paintCell(self, painter, rect, date):
        # Check if the date belongs to the current month and year
        if date.month() == self.monthShown() and date.year() == self.yearShown():
            # Fill the cell with a white background
            painter.fillRect(rect, Qt.white)
            
            painter.setPen(Qt.black)
            calendarWidget = QCalendarWidget()
            
            # Draw the custom day number in the top-left corner
            painter.drawText(rect, Qt.AlignTop | Qt.AlignLeft, str(date.day()))
