from __future__ import print_function

import requests, json
from bs4 import BeautifulSoup

  
URL = "http://www.aberdeenships.com/single.asp?index={}"

details = []
with open('ids.txt') as f:
    ids = f.readlines()

ids = map(str.strip, ids)

for id in ids:
    print('Getting for id', id, )
    r = requests.get(URL.format(id)) 

    if r.status_code <> 200:
        print(r)
        print(r.content)
        print(r.url)
        continue
    
    soup = BeautifulSoup(r.content, 'html5lib') 

    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')

    ship = {'id': id}
    for row in rows:
        field = row.find('h5').getText()
        value = row.findAll('td')[-1].getText()
        ship[field] = value
        if field == "Name":
            print("Name: ", value)
    details.append(ship)
        
with open('ships.json', 'w') as f:
    json.dump(details, f, indent=1)
