from ovchipkaart import ovchiptrx
from tarieven import get_cost
from stations import stationslijst, get_station_code

besteed = 0
zou_kosten = 0
maandprijs = 9900

for trx in ovchiptrx:
    van = trx["Vertrek"]
    naar = trx["Bestemming"]
    try:
        van_code = get_station_code(van)
        naar_code = get_station_code(naar)
    except ValueError as ve:
        print(">>> Warning: skipping transaction between '{}' and '{}'.".format(van,naar))
        print(">>> Warning: {}".format(ve))
        continue

    bedrag = 0 if trx["Bedrag"] == "" else int(trx["Bedrag"].replace(",", ""))
    cost = int(get_cost(van_code, naar_code).replace(",", ""))

    besteed = besteed + bedrag
    zou_kosten = zou_kosten + cost

    print("Van: {}, Naar: {}, Betaald: {:.2f}, Zou kosten: {:.2f}".format(van, naar, bedrag/100, cost/100))

print("Besteed: {:.2f}, Zou kosten: {:.2f}".format(besteed/100, zou_kosten/100))
print("Maandprijs: {:.2f}".format(maandprijs/100))
print("Bespaard: {:.2f}".format((zou_kosten - besteed - maandprijs)/100))
