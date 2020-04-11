from __future__ import print_function

import requests 
from bs4 import BeautifulSoup

  
URL = "http://www.aberdeenships.com/browse.asp?offset={}"

links = []
ids = []

for index in xrange(0, 3104, 20):
    print('Getting from offset ', index)
    r = requests.get(URL.format(index)) 
  
    soup = BeautifulSoup(r.content, 'html5lib') 

    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        link = row.find('a').get('href')
        if 'single' in link:
            links.append(link)
            ids.append(link.split('=')[-1])

with open('ids.txt', 'w') as f:
    for id in ids:
        f.write(id)
        f.write('\n')
