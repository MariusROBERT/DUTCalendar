from my_calendar import import_calendar, MyCalendar

profs = {"M4101C": {"B": "MONTANVERT"}, "M4105C": {"B":"HAMON"}}#, "M4201C": "B", "M4202C": "D"}

def remove_options(calendar: MyCalendar, options: list) -> None:
    for event in calendar.events:
        if event.summary.split()[0] in options:
            calendar.events.remove(event)

def get_cours_from_options(calendar: MyCalendar, options_dict: dict) -> None:
    global profs
    for event in calendar.events:
        for matiere, option in options_dict.items():
            if event.description.find(profs[matiere][option]) != -1:
                print(event.description)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matiere_options = ["M4101C", "M4105C", "M4201C", "M4202C"]
    options_perso = {"M4101C": "B", "M4105C": "B"}# "M4201C": "M4201C", "M4202C": "M4202C"}

    cal = import_calendar("ADECal.ics")
    # remove_options(cal, matiere_options)
    # cal.write("ADECal2.ics")
    get_cours_from_options(cal, options_perso)