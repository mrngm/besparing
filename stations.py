import csv

stationslijst = {}

with open("csv/stations-nl-2017-01.csv") as f:
    dr = csv.DictReader(f, delimiter=',', quotechar='"')
    for line in dr:
        stationslijst[line["code"]] = line

def get_station_code(match):
    for station in stationslijst:
        if stationslijst[station]["naam"] == match:
            return station
    raise ValueError("Could not find station")
