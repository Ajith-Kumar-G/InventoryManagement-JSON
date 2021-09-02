import json
fd = open("inventory.json", "r+")
pdict = json.load(fd)
for i in pdict:
    print(pdict[i]["name"])









