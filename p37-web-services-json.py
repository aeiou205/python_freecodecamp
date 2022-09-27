# JAVASCRIPT OJECT NOTATIOMN
#web services-json
#Java_script object Notation (JSON)
# Objetc literal notation in javascript
import json 
data = '''{
    "name" : "chuck",
    "phone" :{
        "type" : "intl",
        "numer " : "+4333213213"
    },
    "email": {
        "hide":"yes"
   }    
}'''
info = json.loads(data) #cargar desde la cadena
print('Name:' , info ["name"])
print('hide:' , info["email"]["hide"])

# --------lista de 2 diccionarios cochetes
input = '''[
    {
        "id" : "001",
        "x" : "2",
        "name" : "chuck"
    },
    {
        "id" : "009",
        "x"  : "7",
        "name" : "chuck"
    }   
]'''
info = json.loads(input)
print('user count:',len(info))
for item in info:
    print('Name', item['name'])
    print('id', item['id'])
    print('Attribute', item['x'])
