import datetime
from pathlib import Path

class GoodRecord:
    def __init__(self, name: str, date: datetime.date, price: float):
        self.name = name
        self.date = date
        self.price = price

    def __str__(self):
        #return f"{self.name}, {self.date.year}.{self.date.month}.{self.date.day}, {self.price}"
        return f"{self.name}, {self.date}, {self.price}"


records = []
with open(Path(__file__).parent / 'data.txt') as data:
    for record in data.readlines():
        name, date, price = record.split(',')

        name = name.strip()

        year, month, day = [int(a) for a in date.split('-')]
        date = datetime.date(year, month, day)

        price = float(price)

        records.append(GoodRecord(name, date, price))

for r in records: print(r)
