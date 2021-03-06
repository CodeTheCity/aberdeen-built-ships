import json

with open("ships.json") as f:
    built_ships_tbl = json.load(f)

ship_builders = {}
for s in built_ships_tbl:
    builder = ""
    if 'Shipbuilder' in s:
        builder = s['Shipbuilder']
    elif 'Builder' in s:
        builder = s['Builder']
    if builder:
        if builder in ship_builders:
            ship_builders[builder] += 1
        else:
            ship_builders[builder] = 1


print(len(ship_builders), "distinct shipbuilders")

with open("ship_builders.csv", "w") as f:
    f.write("builder, ships built\n")
    for builder, count in ship_builders.items():
        f.write("\""+builder+"\", "+str(count))
        f.write("\n")
