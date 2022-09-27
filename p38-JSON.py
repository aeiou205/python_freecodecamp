import json 
data = '''{
    "name" : "chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+21321321"
        }, 
        "email" : {
        "hide" : "yes"
        }
    }'''
info = json.loads(data)
print('Name:',info["name"])
print('hide:',info["email"]["hide"])

#----
input = '''[
    {
        "id": "001",
        "x" : "2",
        "name" : "chuck"
    },
    {
        "id" : "009",
        "x": "7",
        "name" : "Chuck"
    }
    ]'''
info = json.loads(input)
print('user count:', len(info))
for item in info:
    print('Name', item['name'])
    print('id', item['id'])
    print('Attribute', item['x'])

