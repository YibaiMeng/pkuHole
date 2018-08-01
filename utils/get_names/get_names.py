# get all the names given to the commentators from the only post that had exhausted them all 
import json

with open("42056.json") as fp:
    dat = json.load(fp)

for c in dat["data"]:
    print(c["name"])
# It's then piped for further processing.
