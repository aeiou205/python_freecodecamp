"""
The API itself is largely abstract in that it specifies an 
interface and controls the behavior of the object specified in that
interface. The Software thath provides the functionality
described by an API is said to be an implementation" of the 
api. An API is typically defined in terms of te programming language 
used to build an aplication 

{
    "status": "ok"
        "results":[
            {

            }
        ]
}
"""
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'hhtp://maps.googleapis.com/maps/api/geocode/json'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.pase.urlencode({'address':address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'ok':
        print('====Failure To Retrieve ====')
        print(data)
    iat = js["results"]["results"][0]["geometry"]["location"]["iat"]
    ing = js["result"][0]["geometry"]["location"]["location"]["ing"]
    print('iat' , iat, "ing",ing)
    location = js['results'][0]['formatted_address']
    print(location)    
