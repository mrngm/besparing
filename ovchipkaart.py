import csv

def get_transactions(csvfile):
    ovchiptrx = []
    with open(csvfile) as f:
        dr = csv.DictReader(f, delimiter=';', quotechar='"')
        for line in dr:
            ovchiptrx.append(line)
    return ovchiptrx
