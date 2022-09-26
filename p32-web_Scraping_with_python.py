#What_is_web scraping?
"""when a promagram or scriot pretend to be a browser and retrieves
web pages, look at those web pages, extract information, and the looks at more
web pages
"""
"""
Search enfines scrape web pages - we call this "spidering th web 
or web crawing
"""

#why a Scrape?
"""
->Pull data . praticularly social data - who links to who?
->get your own data back put of some systema that has no export capability
->monitor a site for new information
->spider the web to make a database for a search engine
"""

#Scraping web pages

"""
There is some controversy about web page scraping and some sites are a bit snippy about it
Republishing copyrighted information is no allowed
Violating terms of service is not allowed
"""

#The Easy Way - Beautiful Soup
"""
-> You could do string search the hard wat
-> or use the free software library called BeautifulSoup from
www.crummy.com
"""
 
#BeatifulSoup Installion

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#Retrive all of the anchor tags
tags = soup ('a')
for tag in tags:
    print(tag.get('href',None))
    