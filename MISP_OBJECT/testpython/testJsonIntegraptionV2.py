import json

# a Python object (dict):
x = {
  "values": [
    {
      "description": "CopyCat is a fully developed malware with vast capabilities, including rooting",
      "meta": {
        "refs": [
          "https://blog.checkpoint.com/2017/07/06/how-the-copycat-malware-infected-android-devices-aro"
        ]
      },
      "uuid": "40aa797a-ee87-43a1-8755-04d040dbea28",
      "value": "CopyCat"
    }
    ]
}


# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

x = json.loads(y)



print(x ["values"][0]["description"])



