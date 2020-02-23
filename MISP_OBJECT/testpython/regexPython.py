
import re
import json


searchfile = open("../APT_Digital_Weapon/APT16/README.md", "r")
name, alias, description, references = re.findall("\*\*NAME:\*\*(.*)\*\*Alias\*\*[:]?(.*)\*\*Description\*\*[:]?(.*)\*\*References\*\*[:]?(.*)",searchfile.read(), re.DOTALL)[0]

name = name.strip()
alias = alias.strip()
description = description.strip()
references = references.strip() 

#print(name)
#print(alias)
#print(description)
#print(references)

searchfile.close()

# a Python object (dict):
x = {
  "values": [
    {
      "description": description ,
      "meta": {
        "refs": [
         	references
        ]
      },
      "value":  name  ,
      "alias":  alias
    }
    ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
#print(y)

x = json.loads(y)

#print(x["values"][0]["description"])
print(x["values"][0]["value"])






