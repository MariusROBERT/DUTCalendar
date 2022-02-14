from event import Event, import_event


class MyCalendar:
    def __init__(self, events: list = None):
        self.__events = events if events else []

    def add_event(self, event: Event):
        self.__events.append(event)

    @property
    def events(self):
        return self.__events

    def __str__(self):
        text_start = "BEGIN:VCALENDAR\nMETHOD:REQUEST\nPRODID:MariusROBERT\nVERSION:2.0\nCALSCALE:GREGORIAN\n"
        text_end = "\nEND:VCALENDAR"
        return text_start + "\n".join(str(event) for event in self.__events) + text_end

    def write(self, filename: str):
        with open(filename, "w") as f:
            f.write(str(self))

def import_calendar(file_name: str) -> MyCalendar:
    with open(file_name, 'r') as f:
        text = f.read()
    text = text.split("BEGIN:VEVENT")[1:]
    calendar = MyCalendar()
    for event in text:
        event = import_event(event)
        calendar.add_event(event)
    return calendar

def write_calendar(calendar: MyCalendar, file_name: str):
    with open(file_name, 'w') as f:
        f.write(str(calendar))

if __name__ == "__main__":
    cal = import_calendar("ADECal.ics")
    print(cal)
