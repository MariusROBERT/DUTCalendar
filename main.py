from my_calendar import import_calendar

def remove_options(calendar, options):
    for event in cal.events:
        if event.summary.split()[0] in options:
            calendar.events.remove(event)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options = ["M4101C", "M4105C", "M4201C", "M4202C"]
    cal = import_calendar("ADECal.ics")
    remove_options(cal, options)
    cal.write("ADECal2.ics")
