import csv

this_ship = "Name,Wikidata,ABS_ID_0,ABS_ID_1,ABS_ID_2,ABS_ID_3,ABS_ID_4,ABS_ID_5,ABS_ID_6,ABS_ID_7"
ship_list = []

with open('possibly_already_exist_with_links.txt') as f:
	for line in f:
		
		if line[:4] == "name":
			ship_list.append (this_ship)
			this_ship = "" + line.split(":")[1].strip()

		elif line[:8] == "wikidata":
			this_ship = this_ship + "," + line.split(": ")[1].strip()
			
		elif line[:4] == "http":
			this_ship = this_ship + "," + line.split(' "')[0].strip()

resultFile = open('csv_of_found_ships.csv','w')

for s in ship_list:
    resultFile.write(s + "\n")
resultFile.close()