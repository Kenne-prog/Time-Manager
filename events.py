from PyQt5.QtCore import QDate

#class for events and to manage events
class Events:
    def __init__(self):
        self.events = []  # Store events as a list of dictionaries

    def createEvent(self, title, description, start_date, due_date, estimated_time):
        # Calculate daily time estimate
        delta = due_date.daysTo(start_date)
        if delta > 0:
            daily_estimate = estimated_time / delta
        else:
            daily_estimate = estimated_time

        # Create an event dictionary with details
        event = {
            'title': title,
            'description': description,
            'start_date': start_date,
            'due_date': due_date,
            'estimated_time': estimated_time,
            'daily_estimate': daily_estimate
        }

        self.events.append(event)

    # Add other event-related methods as needed
