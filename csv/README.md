# CSV-bestanden

Onder CC0-licentie via [Rijdendetreinen blog](https://blog.rijdendetreinen.nl/2017/01/afstandenmatrix-januari-2017/)

* `afstandenmatrix-2017-01.csv`
* `afstandenmatrix-2017-01-ns.csv`
* `stations-nl-2017-01.csv`

# Tarieven CSV

Via de [NS tarievenpagina voor consumenten](http://www.ns.nl/klantenservice/betalen/tarieven-consumenten-2017.html),
de [tarieven PDF](http://www.ns.nl/binaries/_ht_1484823524466/content/assets/ns-nl/klantenservice/2017/tarieven-2017.pdf)

Er moet wat preprocessing gedaan worden om de tarieven CSV te kunnen gebruiken:

1. `cd csv/`
1. `pdftotext -layout tarieven-2017.pdf`
2. `echo "tariefeenheid;tweedevol;tweede20;tweede40;eerstevol;eerste20;eerste40" >> tarieven.csv`
3.
```
  for i in {0..8}; 
    do PREPEND=`grep -P '^\s+\d+\b\s+' tarieven-2017.txt | sed -e 's/€/;/g' | tr -d ' ' | head -n 1 | cut -d ';' -f 2-`; 
       echo "$i;$PREPEND" | tee -a tarieven.csv;
  done;
```
4. `grep -P '^\s+\d+\b\s+' tarieven-2017.txt | sed -e 's/€/;/g' | tr -d ' ' | head -n 243 | tail -n +2 >> tarieven.csv`
