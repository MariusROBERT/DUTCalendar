import json

from my_calendar import import_calendar, MyCalendar

profs = {"M4101C": {"B": "MONTANVERT",
                    "C": "RANDOM",
                    "D": "RANDOM"},
         "M4201C": {"B": "BLANCO-LAINE",
                    "C": "CHABOUD",
                    "D": "RANDOM"},
         "M4202C": {"B": "HAMON",
                    "C": "CORSET",
                    "D": "BILLIOT"}
         }

lien_cal_S4B1 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41515&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"
lien_cal_S4B2 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41526&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"
lien_cal_S4C1 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41815&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"
lien_cal_S4C2 = "https://ade-uga.grenet.fr/jsp/custom/modules/plannings/anonymous_cal.jsp?resources=41816&projectId=1&calType=ical&firstDate=2022-02-14&lastDate=2022-04-15"


def remove_options(calendar: MyCalendar, options: list) -> None:
    for event in calendar.events:
        if event.summary.split()[0] in options:
            calendar.events.remove(event)


def delete_other_options(calendar: MyCalendar, options_dict: dict) -> None:
    global profs
    for event in calendar.events:
        for i in profs.keys():  # Pour toutes les options
            if event.summary.find(i) != -1:  # Check si la matière est une matière à options
                # print("matière à options")
                if event.description.find(profs[i][options_dict[i]]) == -1:  # Si l'option n'est pas celle demandée
                    # print("Suppression de l'évènement : " + event.description)
                    calendar.events.remove(event)  # On vire l'event
                    # break  # et on casse la boucle
                # else:
                #     a = 1


if __name__ == '__main__':
    matiere_options = ["M4101C", "M4105C", "M4201C", "M4202C"]
    with open("config.json", "r") as f:
        options_perso = json.load(f)

    cal = import_calendar("ADECal.ics")
    # remove_options(cal, matiere_options)
    # cal.write("ADECal2.ics")
    delete_other_options(cal, options_perso)
    cal.write("ADECal3.ics")
