import json
import wd_mappings

with open('ships.json') as f:
    ships = json.load(f)

def description(s):
    t = s['Type'].title() if 'Type' in s.keys() else 'Ship'
    t = t.replace('\r', '')
    t = t.replace('\n', '')
    if 'Date' in s.keys():
        d = ' in '+s['Date']
    else:
        d = ''
    return '"{t} built in Aberdeen{d}"'.format(t=t, d=d)

already = [x[1] for x in wd_mappings.get_wd_abs_mappings()]

lines = []
for s in ships:
    if s['id'] not in already:
        lines.append(','.join([
            '', #qid
            s['Name'], #Len
            description(s), # Den
            'Q11446', # Instance of ship
            s['Name'], # Name
            s['id'], # ABS ID
            'Q36405']))


with open('qs.csv', 'w') as qs:
    qs.write('qid, Len, Den, P31, P2561, P8260, P1071\n')
    for l in lines:
        qs.write(l)
        qs.write('\n')
    
