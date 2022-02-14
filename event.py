from datetime import datetime, timedelta


class Event:
    def __init__(self, dstart: datetime.date, dend: datetime.date, location: str = "", summary: str = "",
                 description: str = "", dtstamp: datetime.date = None, uid: str = None, created: datetime.date = None,
                 last_modified: datetime.date = None, sequence: int = None):
        if type(dstart) == int:
            self.__dstart = datetime.fromtimestamp(dstart)
        elif type(dstart) == str:
            try:
                self.__dstart = datetime.strptime(dstart, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                try:
                    self.__dstart = datetime.strptime(dstart, "%Y%m%dT%H%M%SZ")
                except ValueError:
                    raise ValueError("Invalid date format")
        elif type(dstart) == datetime:
            self.__dstart = dstart
        else:
            raise TypeError("dstart must be datetime, timestamp or string (%Y-%m-%dT%H:%M:%S)")

        self.__dend = None
        if type(dend) == int:
            self.dend = datetime.fromtimestamp(dend)
        elif type(dend) == str:
            try:
                self.__dend = datetime.strptime(dend, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                try:
                    self.__dend = datetime.strptime(dend, "%Y%m%dT%H%M%SZ")
                except ValueError:
                    raise ValueError("Invalid date format")
        elif type(dend) == datetime:
            self.dend = dend
        else:
            raise TypeError("dend must be datetime, timestamp or string (%Y-%m-%dT%H:%M:%S)")

        self.__location = location
        self.__summary = summary
        self.__description = description
        if type(dtstamp) == int:
            self.__dtstamp = datetime.fromtimestamp(dtstamp)
        elif type(dstart) == str:
            try:
                self.__dtstamp = datetime.strptime(dtstamp, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                try:
                    self.__dtstamp = datetime.strptime(dtstamp, "%Y%m%dT%H%M%SZ")
                except ValueError:
                    raise ValueError("Invalid date format")
        elif dtstamp is None:
            self.__dtstamp = datetime.now()
        # self.__dtstamp = datetime.now() if dtstamp is None elif type(dtstamp)
        self.__uid = self.__dtstamp if uid is None else uid
        self.__created = self.__dtstamp.strftime("%Y%m%dT%H%M%SZ") if created is None else created
        self.__last_modified = self.created if last_modified is None else last_modified
        self.__sequence = 0 if sequence is None else sequence

    @property
    def dstart(self):
        return self.__dstart

    @dstart.setter
    def dstart(self, dstart):
        self.__dstart = dstart
        self.dend = dstart + timedelta(minutes=30)
        self.__last_modified = datetime.now().strftime("%Y%m%dT%H%M%SZ")

    @property
    def dend(self):
        return self.__dend

    @dend.setter
    def dend(self, dend):
        if dend < self.__dstart:
            raise ValueError("End date cannot be before start date")
        self.__dend = dend
        self.__last_modified = datetime.now().strftime("%Y%m%dT%H%M%SZ")

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location
        self.__last_modified = datetime.now().strftime("%Y%m%dT%H%M%SZ")

    @property
    def summary(self):
        return self.__summary

    @summary.setter
    def summary(self, description):
        self.__summary = description
        self.__last_modified = datetime.now().strftime("%Y%m%dT%H%M%SZ")

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
        self.__last_modified = datetime.now().strftime("%Y%m%dT%H%M%SZ")

    @property
    def dtstamp(self):
        return self.__dtstamp

    @property
    def uid(self):
        return self.__uid

    @property
    def created(self):
        return self.__created

    @property
    def last_modified(self):
        return self.__last_modified

    @property
    def sequence(self):
        return self.__sequence

    def __str__(self):
        return f"BEGIN:VEVENT\nDTSTAMP:{self.dtstamp.strftime('%Y%m%dT%H%M%SZ')}\n"+\
        f"DTSTART:{self.dstart.strftime('%Y%m%dT%H%M%SZ')}\nDTEND:{self.dend.strftime('%Y%m%dT%H%M%SZ')}\n"+\
        f"SUMMARY:{self.summary}\nLOCATION:{self.location}\nDESCRIPTION:{self.description}\nUID:{self.uid}\n"+\
        f"CREATED:{self.created}\nLAST-MODIFIED:{self.last_modified}\nSEQUENCE:{self.sequence}\nEND:VEVENT"

    def debug(self):
        print(self.summary)


def import_event(event_str: str) -> Event:
    data = dict()
    infos = ["DTSTAMP", "DTSTART", "DTEND", "SUMMARY", "LOCATION", "DESCRIPTION", "UID", "CREATED", "LAST-MODIFIED", "SEQUENCE", "END"]
    for i in range(len(infos)-1):
        data[infos[i]] = event_str.split(infos[i] + ":")[1].split(f"\n{infos[i + 1]}")[0]
    # data["DESCRIPTION"] = event_str[event_str.find("DESCRIPTION:") + len("DESCRIPTION:"):event_str.find("\nUID:")]

    event = Event(dstart=data["DTSTART"], dend=data["DTEND"], location=data["LOCATION"], summary=data["SUMMARY"],
                  description=data["DESCRIPTION"], dtstamp=data["DTSTAMP"], uid=data["UID"], created=data["CREATED"],
                  last_modified=data["LAST-MODIFIED"], sequence=int(data["SEQUENCE"]))
    return event


if __name__ == "__main__":
    e = Event(
        dstart="2021-01-01T00:00:00",
        dend=datetime.now() + timedelta(minutes=50),
        location="Somewhere",
        summary="Résumé",
        description="Desc"
    )
    print(e)
