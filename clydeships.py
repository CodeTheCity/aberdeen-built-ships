import requests
import csv
from bs4 import BeautifulSoup

builders_list = ['2040', '2042', '2090', '2093', '2127']
all_ships = []


def get_ships(builder_no):
    url = "http://www.clydeships.co.uk/list.php?a1Page=1&a1PageSize=210&builder="

    r = requests.get(url+builder_no)

    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find('table')
    rows = table.find_all('tr', attrs={"class": "Row"})  # two classes ('Row' and 'AltRow')
    for row in rows:
        this_ship = []
        cells = row.find_all('td')
        if len(cells) == 5:
            if cells[0].text:
                this_ship.append(cells[0].get_text(strip=True))
            else:
                this_ship.append(cells[0].get_text(strip=True))
            if cells[1].text:
                this_ship.append(cells[1].get_text(strip=True))
            else:
                this_ship.append("")
            if cells[2].text:
                this_ship.append(cells[2].get_text(strip=True))
            else:
                this_ship.append(cells[2].get_text(strip=True))
            if cells[3].text:
                this_ship.append(cells[3].get_text(strip=True))
            else:
                this_ship.append("")
            if cells[4].text:
                this_ship.append(cells[4].get_text(strip=True))
            else:
                this_ship.append("")
        heads = row.find_all('th')
        if len(heads) == 2:
            # print ("heads0: ", heads[0].text)
            if heads[0].text:
                this_ship.append(heads[0].get_text(strip=True))
            else:
                this_ship.append("")

            if heads[1].text:
                this_ship.append(heads[1].get_text(strip=True))
            else:
                this_ship.append("")  # print (sbs_link)
            el = row.find('a', href=True)
            if el:
                this_ship.append(el['href'])
            else:
                this_ship.append("")
            # print ("heads1: ", heads[1].text)

        if len(this_ship) > 0:
            all_ships.append(this_ship)

    rows = table.find_all('tr', attrs={"class": "AltRow"})
    for row in rows:
        this_ship = []
        cells = row.find_all('td')
        if len(cells) == 5:
            if cells[0].text:
                this_ship.append(cells[0].get_text(strip=True))
            else:
                this_ship.append(cells[0].get_text(strip=True))
            if cells[1].text:
                this_ship.append(cells[1].get_text(strip=True))
            else:
                this_ship.append("")
            if cells[2].text:
                this_ship.append(cells[2].get_text(strip=True))
            else:
                this_ship.append(cells[2].get_text(strip=True))
            if cells[3].text:
                this_ship.append(cells[3].get_text(strip=True))
            else:
                this_ship.append("")
            if cells[4].text:
                this_ship.append(cells[4].get_text(strip=True))
            else:
                this_ship.append("")
        heads = row.find_all('th')
        if len(heads) == 2:
            # print ("heads0: ", heads[0].text)
            if heads[0].text:
                this_ship.append(heads[0].get_text(strip=True))
            else:
                this_ship.append("")

            if heads[1].text:
                this_ship.append(heads[1].get_text(strip=True))
            else:
                this_ship.append("")  # print (sbs_link)
            el = row.find('a', href=True)
            if el:
                this_ship.append(el['href'])
            else:
                this_ship.append("")

            # print ("heads1: ", heads[1].text)

        # print(this_ship)
        all_ships.append(this_ship)

for builder in builders_list:
    get_ships(builder)

print(all_ships)

csv_filename = 'SBS_Duthies.csv'
fieldnames = ['Year', 'Order_Num', 'Yard_Num', 'Vessel_Type', 'Propulsion', 'Vessel_Name', 'Builder', 'SBS_link']
with open(csv_filename, mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in all_ships:
        writer.writerow({fieldnames[0]: i[0], fieldnames[1]: i[1], fieldnames[2]: i[2], fieldnames[3]: i[3], fieldnames[4]: i[4], fieldnames[5]: i[5], fieldnames[6]: i[6], fieldnames[7]: i[7]})
