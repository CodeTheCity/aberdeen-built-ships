from __future__ import print_function

import json
import pandas as pd

harbour_ships_tbl = pd.read_csv("http://www.tulip.asae.co.uk/api/v1.0/vessels.csv")

harbour_ships = set()
for v in harbour_ships_tbl.vessel.items():
    harbour_ships.add(str(v[1]).upper())

with open("ships.json") as f:
    built_ships_tbl = json.load(f)

built_ships = set()
for s in built_ships_tbl:
    if s.has_key('Name'):
        built_ships.add(s['Name'].upper())

arrived_and_built = harbour_ships & built_ships

print(len(harbour_ships), "ships names seen in harbour arrivals.")
print(len(built_ships), " ships names in built list")
print(len(arrived_and_built), " ships on both lists")

with open("arrived_and_built.txt", "w") as f:
    for s in arrived_and_built:
        f.write(s)
        f.write("\n")
