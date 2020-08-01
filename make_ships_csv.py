import json, csv

with open('ships.json') as f:
    ships = json.load(f)

fields = ['Name', 'Date', 'Type', 'Shipbuilder', 'Builder', 'Official Number', 'Construction', 'id',
          'Dimensions', 'Owner', 'Shipowner',
          'Associated', 'Description']

def make_row(ship, fields):
    return [ship[f] if f in ship.keys() else '' for f in fields]

with open('ships.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for s in ships:
        row = make_row(s, fields)
        if row:
            writer.writerow(row)
        else:
            print(s)
