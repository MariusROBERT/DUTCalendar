from my_calendar import import_calendar, MyCalendar

profs = {"M4101C": {"B": "MONTANVERT"},
         "M4105C": {"B": "ORTEGA",
                    "C":"DAILLY",
                    "D": "LAURILLAU"},
         "M4201C": {"C": "CHABOUD",
                    "B": "BLANCO-LAINE"},
         "M4202C": {"B": "HAMON",
                    "D": "BILLIOT",
                    "C": "CORSET"}
         }
lien_cal_S4B1 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41515&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"
lien_cal_S4B2 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41526&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"
lien_cal_S4C1 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41815&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"
lien_cal_S4C2 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41816&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"


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


if __name__ == '__main__':
    matiere_options = ["M4101C", "M4105C", "M4201C", "M4202C"]
    options_perso = {"M4101C": "B", "M4105C": "B"}  # "M4201C": "M4201C", "M4202C": "M4202C"}

    cal = import_calendar("ADECal.ics")
    # remove_options(cal, matiere_options)
    # cal.write("ADECal2.ics")
    get_cours_from_options(cal, options_perso)
