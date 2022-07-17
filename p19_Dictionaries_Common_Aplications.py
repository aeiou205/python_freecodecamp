#------------------Many Counters With a Dictionary------------------------------
#one common use of dictionaries is counting how often we "see" something
nuevdictionary = dict()
nuevdictionary['marker1'] = 1
nuevdictionary['marker2'] = 1
print(nuevdictionary)
nuevdictionary['marker1'] = nuevdictionary['marker1'] + 1
print(nuevdictionary)

#-------Dictionary Tracebacks
#Itis an error to reference a key wich is not in the dictionary 
#we can use the in operator to see if a key is in the dictionary


#diccionary = dict()
#print(diccionary['csev'])

#---------when we see a new name-----------------------------------------------
#
#when we encounter a new name, we need to add a new entrey in the
#dictionary and if this the second or later time we have seen the name
#we simply add one to the count in the dictionary under thah name

count = dict() #declarar el espacio en memoria del diccionario
names = ['csv', 'cwen', 'squian', 'cwen', 'csv'] #declaracion del diccionario con todos las eqtiquetas
for names in names :
    if names not in count: #si NO aparece la eqtiqueta en el diccionario count
        count[names] = 1 #agrega algo nuevio
    else : # si si esta
        count[names] = count[names] + 1 #le da valor a la eqtiqueta que si existe
print("hola",count) #imprime los valores


#-------The "get" methos for dictionaries-----------------------------------
#--The get method for dictionaries
#---Default value if key does not exist
#---(and no Traceback)
if names in count:
    x = count[names]
else :
    x = 0

x = count.get(names,0)
print(x)

#--------Simplified counting with get()----------------------------------
#---we can use get() and provide a default value of zero when the key 
#---is not yet in the dictionary -and then just add one
count = dict()
names = ['csv', 'cwen', 'squian', 'cwen', 'csv']
for names in names :
    count[names] = count.get(names,0) + 1
print(count)






 
