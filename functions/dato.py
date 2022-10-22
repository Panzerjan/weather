from datetime import datetime

class date():

    def __init__(self):
        self.date = datetime.now()

    def get_now_date(self):
        date = self.date
        return date

    def get_date(self):
        now = self.date
        dato = now.strftime("%Y-%m-%d")
        return dato


