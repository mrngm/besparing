from ovchipkaart import get_transactions
from tarieven import get_cost
from stations import stationslijst, get_station_code

import argparse

besteed = 0
zou_kosten = 0

parser = argparse.ArgumentParser(description=u"Shows 'money well spent' for your OV chipcard subscription.")
parser.add_argument('--csv', metavar='CSV', required=False,
                    dest='csv', help=u'Load this csv file instead of the default',
                    default='csv/transacties-ovchip.csv')
parser.add_argument('--silent', '-s', default=False, action="store_true",
                    help=u'Do not show individual transactions, but only totals')
parser.add_argument('--price', '-p', metavar='PRICE', type=int, default=9900, required=False,
                    dest='price', help=u'Monthly price of your season ticket in eurocents')

args = parser.parse_args()

ovchiptrx = get_transactions(args.csv)

for trx in ovchiptrx:
    if trx["Transactie"] == "Check-in":
        continue
    elif trx["Transactie"] == "Saldo opgeladen":
        continue
    elif trx["Vertrek"] == trx["Bestemming"]:
        continue

    van = trx["Vertrek"]
    naar = trx["Bestemming"]
    try:
        van_code = get_station_code(van)
        naar_code = get_station_code(naar)
    except ValueError as ve:
        if not args.silent:
            print(">>> Warning: skipping transaction between '{}' and '{}'.".format(van,naar))
            print(">>> Warning: {}".format(ve))
        continue

    bedrag = 0 if trx["Bedrag"] == "" else int(trx["Bedrag"].replace(",", ""))
    try:
        cost = int(get_cost(van_code, naar_code).replace(",", ""))
    except ValueError as ve:
        if not args.silent:
            print(">>> Warning: skipping transaction between '{}' and '{}'.".format(van,naar))
            print(">>> Warning: {}".format(ve))
        continue

    besteed = besteed + bedrag
    zou_kosten = zou_kosten + cost

    if not args.silent:
        print("Van: {}, Naar: {}, Betaald: {:.2f}, Zou kosten: {:.2f}".format(van, naar, bedrag/100, cost/100))

print("Besteed: {:.2f}, Zou kosten: {:.2f}".format(besteed/100, zou_kosten/100))
print("Maandprijs: {:.2f}".format(args.price/100))
print("Bespaard: {:.2f}".format((zou_kosten - besteed - args.price)/100))
