# OV-Chipkaart besparingbepaler

Lees de README.md in `csv/` en zorg ervoor dat de `tarieven.csv` aanwezig is.
Download een transactie-overzicht vanaf https://www.ov-chipkaart.nl/home.htm en
zet dit bestand in `csv/transacties-ovchip.csv`.

Daarna volstaat:

```
$ python besparing.py
Van: Den Helder, Naar: Enschede, Betaald: 0.00, Zou kosten: 26.20
[..]
Besteed: 0.00, Zou kosten: 133.70
Maandprijs: 99.00
Bespaard: 34.70
```
