from __future__ import print_function

import json

with open("ships.json") as f:
    abdn_ships_tbl = json.load(f)

with open("all_wd_ships.json") as f:
    wd_ships_tbl = json.load(f)
    
abdn_ships = {}
for s in abdn_ships_tbl:
    if s.has_key('Name'):
        if abdn_ships.has_key(s['Name']):
            abdn_ships[s['Name']].append(s['id'])
        else:
            abdn_ships[s['Name']] = [s['id']]

for wds in wd_ships_tbl:
    name = wds['ship']['label'].upper()
    if abdn_ships.has_key(name):
        q = wds['ship']['value']
        print(name, " might already exist in wikidata: ", q,
              " id(s): ", abdn_ships[name])
