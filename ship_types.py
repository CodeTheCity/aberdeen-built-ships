from __future__ import print_function

import json

with open("ships.json") as f:
    built_ships_tbl = json.load(f)

ship_types = {}
for s in built_ships_tbl:
    type = ""
    if s.has_key('Type'):
        type = s['Type']
    elif s.has_key('type'):
        type = s['type']
    if type:
        if type in ship_types:
            ship_types[type] += 1
        else:
            ship_types[type] = 1


print(len(ship_types), "distinct shiptypes")

with open("ship_types.csv", "w") as f:
    f.write("type, ships built\n")
    for type, count in ship_types.items():
        f.write("\""+type+"\", "+str(count))
        f.write("\n")
