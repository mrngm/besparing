import csv

ovchiptrx = []

with open("csv/transacties-ovchip.csv") as f:
    dr = csv.DictReader(f, delimiter=';', quotechar='"')
    for line in dr:
        ovchiptrx.append(line)
