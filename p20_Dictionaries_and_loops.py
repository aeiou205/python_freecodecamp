#--------------counting Pattern-------------
counts = dict()
print("enter a line of text:")
line =input('')

words = line.split() #dividimos las palabras del texto

print("words:", words)

print("Counting")
for word in words:
    counts[word] = counts.get(word,0) + 1 #busca la palabra para ver cuantas se repite
print('Counts', counts) #imprimimos el diccionario

#------Define Loops and Dicitionaries
#Even thougt dictionaries are not stored in oprder, we can write a for 
#loop that goes through all the entries in a dictionary - actually it goes
#througth all of the keys in the dictionary and looks up the
#values

count = {'danie':1 , 'suarez':2 ,'NAVA':3, 'JAN':100}
for key in count: #key = clave
    print(key , count[key]) 

#-------Retrieving list of keys and values 
#you can get a list of keys, values, or items(both) from dictionary

danie_dicionari = {'haka':0, 'haka':1, 'Dm':2000}
print(list(danie_dicionari))  #comvertira un diccionario en lista 
#extare los valores del dicccionario y salen en el mismo orden 
print(danie_dicionari.values())
print(danie_dicionari.items()) 


#+++++Busqueda de diccionarios 
fname = input('Enter name file: ')
handle = open(fname)

conta = dict()
for line in handle:
    words = line.split()
    for word in words:
        conta[word] = conta.get(word,0) + 1

bigcount = None 
bigword = None
for word,conta in conta.items():
    if bigcount is None or conta > bigcount:
        bigword = word
        bigcount = conta
print(bigword,bigcount)
       


