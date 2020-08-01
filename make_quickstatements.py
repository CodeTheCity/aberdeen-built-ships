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
with open('qs.tsv', 'w') as qs:
    for s in ships:
        if s['id'] not in already:
            if s['Name'] not in ['', 'UNKNOWN', 'UNNAMED']:
                qs.write('CREATE\n')
                qs.write('LAST\tLen\t"{}"\n'.format(s['Name']))
                qs.write('LAST\tDen\t{}\n'.format(description(s)))
                qs.write('LAST\tP31\tQ11446\n')
                qs.write('LAST\tP8260\t"{}"\n'.format(s['id']))
                qs.write('LAST\tP1071\tQ36405\n')
                qs.write('LAST\tP571\t+{}-01-01T00:00:00Z/9\n'.format(s['Date']))

