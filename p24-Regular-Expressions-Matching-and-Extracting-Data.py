#Matching and Extracting Data

#re. search() returns a True / Falase depending on whether the string matches the regular expression
#if we actually wnat the matching string to be extracted, we use 
# re.find( )

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
#[0-9]+ "uno o mas digitos" en x

#Matching and Extracting Data
#When we use re.findall(), it return a list of of more sub-string
#thath match the regular expression


x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y= re.findall('[AEIOU]+',x)
print(y)

