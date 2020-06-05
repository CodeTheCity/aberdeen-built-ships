This project started at [Code the City 19 History and Data event](https://codethecity.org/what-we-do/hack-weekends/code-the-city-19-history-data-innovation/). 

It's purpose is to gather data on [Aberdeen-built ships](http://www.aberdeenships.com), with the permission of the site's owners, and to push that bulk of data onto [Wikidata](https://www.wikidata.org) as open data, with links back to the Aberdeen Ships site through using a new identifier. 

# Progress to date

### updated 05 Jun 2020

So far the following has been accomplished.

- The script [get_ids.py](get_ids.py) gathers all the ship IDs from [Aberdeen-built ships](http://www.aberdeenships.com) and writes them to [ids.txt](ids.txt).
- The script [get_details.py](get_details.py) uses the IDs from [ids.txt](ids.txt) and scrapes the full ship information from [Aberdeen-built ships](http://www.aberdeenships.com) and writes it to the file [ships.json](ships.json). 
- The file [query.rq](query.rq) contains code to execute a query on [Wikidata Query Service](https://query.wikidata.org) to get the QID and name of every ship on Wikidata. This has been manually downloaded as [all_wd_ships.json](all_wd_ships.json). 
- The file [ship_builders.py](ship_builders.py) checks [ships.json](ships.json) and constructs a list of all ship builders and a frequency count of their appearance, writing it out to [ship_builders.csv](ship_builders.csv).
- The file [already_in_wd.py](alread_in_wd.py) has checked for ships names in [ships.json](ships.json) and crossed matched with [all_wd_ships.json](all_wd_ships.json) and generated a [list of ships](possibly_already_exist_with_links.txt) whose name indicates that they MAY be already in Wikidata. 
- An identifier for Aberdeen Built Ships, P8260, has now been [created in Wikidata](https://www.wikidata.org/wiki/Property:P8260)
- The the [list of all 904 ships](possibly_already_exist_with_links.txt) that possibly existed in Wikidata has been manually checked. the resulting [list of 59 positive matches](Matches_WD_ABS.csv) has been created with a one-to-one mapping between Wikidata entry and ABS ids. 
- The file [ship_types.py](ship_types.py) checks [ships.json](ships.json) and constructs a list of all ship types and a frequency count of their appearance, writing it out to [ship_types.csv](ship_types.csv). Currently there are 207 distinct types of ship!! 

# Next Steps?
To complete the project the following needs to be done

- Rationalise all ship builders that exist in [ship_builders.csv](ship_builders.csv) - deduplicating these and create Wikidata entries for each we will use. 
- Rationalise all ship types that exist in [ship_types.csv](ship_types.csv) - deduplicating these and create Wikidata entries for each we will use. 
- Isolate ships that have no Wikidata identifier - i.e. any one not in the [list of 59 positive matches](Matches_WD_ABS.csv). Set aside those which have entries for later processing. 
- Decide on best route to bulk upload - eg Quickstatements. This may be useful: [Wikidata Import Guide](https://www.wikidata.org/wiki/Wikidata:Data_Import_Guide)
- Agree a core set of data for each ship that will parsed from [ships.json](ships.json) to be added to Wikidata. See _Wikidata Ship Properties_ below. 
- Create a script to output text that can be dropped into a CSV or other file to be used by QuickStatements (assuming that to be the right tool) for bulk input ensuring links for shipbuilder IDs and ABS identifiers are used. 
- deal with adding data to existing 59 wikidata entries 
- Develop a means of monitoring both the original ABS system (rescrape periodically and do a diff on the file in some way? ) and monitor Wikidata for changes to the ships records (Wikidata query, executed periodically, generating a CSV download and checked for differences from previous runs?) to feed back to ABS. 


# Wikidata Ship Properties

The following have been identified as potential Wikidata statements that we need to consider using. Not all ships will have all data available. Core ones have __(*)__ after them.

1. Label __(*)__
2. Description __(*)__
3. Instance of (P31) __(*)__
 - Ship or if available a subclass such as 
 - Schooner
 - Clipper
 - Whaler
 - Brig etc. 
 Note - this can be multiples. 
4. Name (P2561) - or official name (P1448)?? - __(*)__ could have multiple values with dates for start + end
5. Abedeen Built Ships ID (P8260) __(*)__
6. Significant event (P793)
Include possible such as order (Q566889), keel laying (Q14592615), ceremonial ship launching (Q596643), ship decomissioning (Q7497952), shipwrecking (Q906512), but also sea voyage etc. each with point in time (P585). Voyages could have destination and start and end dates. Also destruction, breaking up etc.
7. Cost (P2130)
8. Mass (P2067)
9. Gross Tonnage (P1093)
9. Length (P2043)
9. Beam (P2261)
10.Draft (P2262)
11. Number of masts (P1099)
12. Speed (P2052)
13. Manufacturer (P176) - take values from table of Ship builders
14. location of creation (P1071) -  Aberdeen (Q36405) __(*)__ 
15. Country of origin (P495) - GB 1701-1801, UK GBNI 1801-1927, UK (1927-) __(*)__
16. Service entry (P729)
17. Service Retirement (P730)
18. Described at URL (P973) with a link to ABS (maybe not given we'll have specific ABS ID)
19. Country of Registry (P8047) - could have numerous values / dates
20. Home port (P504)  - could have numerous values / dates


