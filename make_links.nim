import re, os

proc readPoss(filename: string) =
  let pattern = re"(.+)  might already exist in wikidata:  (.+)  id\(s\):  \[(.+)\]"
  let idPattern = re"u'(\d+)'"
  var matches: array[3, string]
  var idMatch: array[1, string]
  for line in filename.lines:
    let start = find(line, pattern, matches)
    if start >= 0:
      echo("name: ", matches[0])
      echo("wikidata: https://wikidata.org/wiki/", matches[1])
      for id in findAll(matches[2], idPattern):
        discard find(id, idPattern, idMatch)
        echo("http://www.aberdeenships.com/single.asp?index=", idMatch[0],
             " \"", idMatch[0], "\" : \"", matches[1], "\"")
    
    

when isMainModule:
  const file = "possibly_already_exist.txt"
  let filename = getCurrentDir() / file
  readPoss(filename)

