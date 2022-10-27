import re
jsonFile = (open('input.json', 'r', encoding="utf8").read())
outputYml = open('output3.yml', 'w', encoding="utf8")

jsonMatch = r'{|},|\[|\],|]|}|\"'
jsonFile_new = re.sub(jsonMatch, '', str(jsonFile))
outputYml.write(jsonFile_new)
outputYml.close()