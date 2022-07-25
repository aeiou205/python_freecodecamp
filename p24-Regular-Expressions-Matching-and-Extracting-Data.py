
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

x= 'From: Using The : character'
y = re.findall('^F.+:', x)
print(y)
#  ^F First characters in the match is an f
#  .+ One more characters
#   : Last character in the match is a:

#me falto 1
