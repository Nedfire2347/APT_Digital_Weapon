from pathlib import Path
import re
import json

li_readme =[]
data = []


for p in Path('../APT_Digital_Weapon').glob('./**/*'):
	if p.is_file():
		if ".git" not in str(p):		
			if "README.md" in str(p):
				li_readme.append(str(p))


#print (li_readme)
for filename in li_readme: 
	print (filename)
	searchfile = open(filename, "r")

	try:
		name, alias, description, references = re.findall("\*\*NAME:\*\*(.*)\*\*Alias\*\*[:]?(.*)\*\*Description\*\*[:]?(.*)\*\*References\*\*[:]?(.*)",searchfile.read(), re.DOTALL)[0]
	except:
	#if alias unsetted
		searchfile.close()
		searchfile = open(filename, "r")
		name, description, references = re.findall("\*\*NAME:\*\*(.*)\*\*Description\*\*[:]?(.*)\*\*References\*\*[:]?(.*)",searchfile.read(), re.DOTALL)[0]
		alias = ""

	name = name.replace("**Probably operating from**:" , "") #Not used in these taxonomy
	name = name.strip()
	alias = alias.strip()
	description = description.strip()
	references = references.strip() 

	searchfile.close()
# a Python object (dict):
	x = {
		"values": [
			{
			"description": description,
			"meta": { 
				"refs": [references] },
				"value":  name  ,
				"alias":  alias 
			}
		]
	}
	data.append(x)

#print(data)

# convert into JSON:
y = json.dumps(data)

# the result is a JSON string:
with open('taxonomy.json', 'w') as dataL:
	json.dump(data, dataL, ensure_ascii=False)

dataL.close()

x = json.loads(y)

#print(x["values"][0]["description"])

# the result is a JSON string:
with open('nameAttack.txt', 'w') as dataL:
	for r in x:
		attack = r["values"][0]["value"]
		print(attack)
		dataL.write(attack + "\n")
dataL.close()		












