#Matching and Extracting Data

#re. search() returns a True / Falase depending on whether the string matches the regular expression
#if we actually wnat the matching string to be extracted, we use 
# re.find( )

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
