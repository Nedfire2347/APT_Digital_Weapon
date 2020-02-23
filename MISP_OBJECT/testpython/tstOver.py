import json

data = [ { 'name':'john' } , { 'name':'paulo' }  ]
var = 21
data[0]["age"] = var

print ('DATA:', repr(data) )

print ('Repr:', repr(data[0]["name"] ) )

print ('Repr:', repr(data[1]["name"] ) )

ty = 'name'
var = "johny"
data.append({ty:var})

print ('Repr:', repr(data[2]["name"] ) )


y = json.dumps(data)

# the result is a JSON string:
print (y)

# Loadings the JSON string:
yy = json.loads(y)

#print ( 'JSON', yy )

print('NAME 2', yy[0]["name"] ) 


with open('data.json', 'w') as y:
    json.dump(data, y, ensure_ascii=False)

