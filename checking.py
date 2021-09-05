import json
fd = open("inventory.json", "r")
Sd = open("productSales.json", 'r')
od = open("outOfStock.json", 'r')
pdict = json.load(fd)
sdict = json.load(Sd)
odict = json.load(od)
k = 1
for i in pdict:
    print(str(k) + ". " + pdict[i]["name"])
    k += 1
for i in sdict:
    print(i, sdict[i])
for i in odict:
    print(i, odict[i])









