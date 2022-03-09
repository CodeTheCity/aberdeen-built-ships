import json
import csv
import mkwikidata

with open("./ships.json") as f:
  SHIPS = json.load(f)
with open("./ship_builders_qids.csv") as f:
  SHIP_BUILDERS = list(csv.DictReader(f))


QUERY = """
SELECT DISTINCT ?item ?itemLabel ?asid WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  {
    ?item wdt:P8260 ?asid.
    MINUS {
      ?item p:P176 _:anyValueP176.
    }
  }
}
"""


def main():
  ships = {}
  for ship in SHIPS:
    ships[ship["id"]] = ship

  builders = {}
  for builder in SHIP_BUILDERS:
    builders[builder["builder"]] = builder

  out = []

  result = mkwikidata.run_query(QUERY)
  for res in result["results"]["bindings"]:
    ship_qid = res["item"]["value"].lstrip("http://www.wikidata.org/entity/")
    ship_id = res["asid"]["value"]
    ship = ships.get(ship_id)
    if not ship:
      print(f"Unknown ship ID {ship_id}")
      continue

    shipbuilder = ship.get("Shipbuilder")
    if not shipbuilder:
      print(f"No known shipbuilder for {ship_id}")
      continue

    builder = builders.get(shipbuilder)
    if not builder:
      print(f"Unknown builder {shipbuilder}")
      continue

    builder_qid = builder.get("QID")
    if not builder_qid:
      print(f"No known QID for builder {shipbuilder}")
      continue

    out.append((ship_qid, "P176", builder_qid, "S143", "Q90807948"))

  print("\n".join(map(lambda o: "|".join(o), out)))

if __name__ == "__main__":
  main()
