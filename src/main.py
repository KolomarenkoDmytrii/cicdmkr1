import datetime
from pathlib import Path
from itertools import groupby

class GoodRecord:
    def __init__(self, name: str, date: datetime.date, price: float):
        self.name = name
        self.date = date
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.date}, {self.price}"


def read_last_month_records(data_file) -> list[GoodRecord]:
    records = []
    with open(data_file) as data:
        for record in data.readlines():
            name, date, price = record.split(',')

            name = name.strip()

            year, month, day = [int(a) for a in date.split('-')]
            date = datetime.date(year, month, day)

            price = float(price)

            records.append(GoodRecord(name, date, price))

    # for the last year
    last_year = max(records, key=lambda record: record.date.year).date.year
    records = list(filter(lambda record: record.date.year == last_year, records))

    # for the last month in the last year
    last_month = max(records, key=lambda record: record.date.month).date.month
    records = list(filter(lambda record: record.date.month == last_month, records))

    return records


def group_by_name(records):
    grouped = []
    for k, g in groupby(records, key=lambda record: record.name):
        grouped.append((k, list(g)))

    return grouped

records = read_last_month_records(Path(__file__).parent / 'data.txt')
# for r in records: print(r)

for g in group_by_name(records):
    print(g[0], ":")
    for a in g[1]:
        print("\t", a)
