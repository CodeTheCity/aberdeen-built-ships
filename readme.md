This project started at [Code the City 19 History and Data event](https://codethecity.org/what-we-do/hack-weekends/code-the-city-19-history-data-innovation/). 

It's purpose is to gather data on [Aberdeen-built ships](http://www.aberdeenships.com), with the permission of the site's owners, and to push that bulk of data onto [Wikidata](https://www.wikidata.org) as open data, with links back to the Aberdeen Ships site through using a new identifier. 

# Progress to date
So far the following has been accomplished.

- The script [get_ids.py](get_ids.py) gathers all the ship IDs from [Aberdeen-built ships](http://www.aberdeenships.com) and writes them to [ids.txt](ids.txt).
- The script [get_details.py](get_details.py) uses the IDs from [ids.txt](ids.txt) and scrapes the full ship information from [Aberdeen-built ships](http://www.aberdeenships.com) and writes it to the file [ships.json](ships.json). 
- The file [query.rq](query.rq) contains code to execute a query on [Wikidata Query Service](https://query.wikidata.org) to get the QID and name of every ship on Wikidata. This has been manually downloaded as [all_wd_ships.json](all_wd_ships.json). 
- The file [ship_builders.py](ship_builders.py) checks [ships.json](ships.json) and constructs a list of all ship builders and a frequency count of their appearance, writing it out to [ship_builders.csv](ship_builders.csv).
- The file [already_in_wd.py](alread_in_wd.py) has checked for ships names in [ships.json](ships.json) and crossed matched with [all_wd_ships.json](all_wd_ships.json) and generated a [list of ships](possibly_already_exist_with_links.txt) whose name indicates that they MAY be already in Wikidata. 

# Next Steps?
To complete the project the following needs to be done

- Enure that the request for an identfier for ABS is created for use by us in adding ships to Wikidata. See below. 
- Create Wikidata entities for all ship builders and note the QID for each. We've already loaded [nine of these](https://w.wiki/Mc9) into WikiData.
- Decide on how to deal with the [list of ships](possibly_already_exist_with_links.txt) that MAY be already in Wikidata. This may be a manual process. Think about how we reconcile this - name / year / tonnage may all be useful. 
- Decide on best route to bulk upload - eg Quickstatements. This may be useful: [Wikidata Import Guide](https://www.wikidata.org/wiki/Wikidata:Data_Import_Guide)
- Agree a core set of data for each ship that will parsed from [ships.json](ships.json) to be added to Wikidata - e.g. name, year, builder, tonnage, length etc
- Create a script to output text that can be dropped into a CSV or other file to be used by QuickStatements (assuming that to be the right tool) for bulk input ensuring links for shipbuilder IDs and ABS identifiers are used. 


## Wikidata Identifier
A request to [create an identifier](https://www.wikidata.org/wiki/Wikidata:Property_proposal/Aberdeen_Built_Ships_ID) for Aberdeen Ships is currently pending. 