import csv

te = {}
mtx = {}

def get_te(van, naar):
    if van in mtx:
        if naar in mtx[van]:
            if mtx[van][naar] == "XXX": 
                return -1
            if mtx[van][naar] == "?":
                return -2
            return int(mtx[van][naar])
    raise KeyError

def get_tariff(tariefeenheid):
    if tariefeenheid == -1:
        raise ValueError("From and to stations are equal.")
    if tariefeenheid == -2:
        raise ValueError("From and to stations have no tariff.")
    if tariefeenheid in te:
        return te[tariefeenheid]
    raise ValueError("Tariefeenheid beyond scope: {}".format(type(tariefeenheid)))

def format_tariff(tariff, tariffdict):
    if not "tweedevol" in tariffdict:
        raise ValueError("Missing tariff information in dictionary")
    return """Tarieven voor tariefafstand {}:
Tweede klas:
  Vol tarief:  {}
  20% korting: {}
  40% korting: {}
Eerste klas:
  Vol tarief:  {}
  20% korting: {}
  40% korting: {}""".format(tariff, tariffdict["tweedevol"], tariffdict["tweede20"],
                            tariffdict["tweede40"], tariffdict["eerstevol"],
                            tariffdict["eerste20"], tariffdict["eerste40"])

def get_cost(van, naar, kind="tweedevol"):
    t = get_tariff(get_te(van, naar))
    if kind in ["tweedevol", "tweede20", "tweede40",
                "eerstevol", "eerste20", "eerste40"]:
        return t[kind]
    raise ValueError("Unexpected kind")

with open("csv/tarieven.csv") as f:
    csvr = csv.reader(f, delimiter=';')
    for line in csvr:
        tarief = line[0]
        if tarief == "tariefeenheid":
            continue
        tweedevol = line[1]
        tweede20 = line[2]
        tweede40 = line[3]
        eerstevol = line[4]
        eerste20 = line[5]
        eerste40 = line[6]
        te[int(tarief)] = { 'tweedevol': tweedevol, 'tweede20': tweede20, 'tweede40': tweede40,
                            'eerstevol': eerstevol, 'eerste20': eerste20, 'eerste40': eerste40 }

with open("csv/afstandenmatrix-2017-01-ns.csv") as f:
    dr = csv.DictReader(f, delimiter=',')
    for line in dr:
        mtx[line["Station"]] = line
