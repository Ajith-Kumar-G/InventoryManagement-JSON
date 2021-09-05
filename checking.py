import json
import pandas as pd
with open("inventory.json") as f:
    pdict = json.load(f)

k = 1
for i in pdict:
    print(str(k) + ". " + pdict[i]["name"])
    k += 1

'''df = pd.read_json('inventory.json')
print(df.values)'''









