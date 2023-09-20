from PyQt5.QtCore import QDate

#class for events and to manage events
class Events:
    def __init__(self):
        self.events = []  # Store events as a list of dictionaries

    def create(self, title, description, time_unit, time_duration, start_date, end_date):

        event = {
            'title': title,
            'description': description,
            'time_unit': time_unit,
            'time_duration': time_duration,       
            'start_date': start_date,
            'end_date': end_date,
        }

        self.events.append(event)

    # Add other event-related methods as needed
