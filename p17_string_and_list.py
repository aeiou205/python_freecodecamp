
#----------Best Friends: Strins and Lists-------
#----------comverter of string in list
abc = 'with three word'
stuff = abc.split()# split breaks string parts and produces a list of string
print(stuff)
print(len(stuff))
print(stuff[0])
###and with taht , we can access a string part list 
#Example
print(stuff)
for w in stuff :
    print(w)

#--------OF SPACES---------
#when you do not specify a delimiter,multiple spaces are
#treated like one delimiter
#We can specific delimiter characters to use in the spliting

line = 'A lot'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()#separar texto oour cadenas
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))
print(len(thing))

###----------
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()#busca email
    if not line.startswith('From') : continue
    word = line.split()
    print(word[2])
line = 'From stephen.marquard@uct.ac.za jan 5 09:14:16 2008'
words = line.split()
print(words)

#---The Double Split Pattern
line = 'From stephen.marquard@uct.ac.za jan 5 09:14:16 2008'
words = line.split() #divide las palabras con un split
email = words[1] 
pieces = email.split('@') 
print(pieces[1])
 











