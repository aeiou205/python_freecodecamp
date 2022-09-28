#Api Security and rate Limiting

#The compute resources to run these APIS are not "free"
#The data provied by these APis is usually valuable
#The data provierders migth limit the number of request per day.
#demand an API "Key", or even charge for usage
#They migth change the rules as things progress

import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITER_URL = 'https://api.twitter.com/1.1/friends/list.json'
while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITER_URL,{screnn_name:acct, 'count': 's'})
    print('Rerieving',url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining',headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('',s[:50])
