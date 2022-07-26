#String parsing String--------------------
#Extracting a host name - using find and string
#Extracción de un nombre de host - usando find y string
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
#hola
appos = data.find('',atpos)
print(appos)

host = data[ atpos+1 : appos]
print(host)


