import datetime

class Expiry:
    def __init__(self, entries):
        self.entries = entries

    def finaldate(self):
        today = datetime.datetime.now()
        finaldate = today + self.entries
        return finaldate


week = int(input('Weeks: '))
day = int(input('Days: '))
hour = int(input('Hours: '))




test1 = Expiry(datetime.timedelta(weeks=week, days=day, hours=hour))


print(test1.finaldate())