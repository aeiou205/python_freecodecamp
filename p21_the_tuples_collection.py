#### TUPLES ARE L9IKE LIST------------
#tuples are another kind of secuence that functions much like a list
#they have elements which are indexed starting at 0

x = ('Glenn', 'sally', 'Josept') #tuples de string
print(x[2]) #imprime elemento 3

y = (1, 9, 2) # tuples de numbers
print(y) 
print(max(y)) #imprime el valor mas grande

#-----but...TUples are "immutable"-----------------
#unlike a list once you create a tuple, you cannot alter its
#contents -similiar to string 

x = [9, 8, 7]
x[2] = 6
print(x) 
[9, 8, 6]

#y = 'ABC'    #----------->EROOR
#y[2] = 'D'

#Z = (5, 5, 3)#-----------ERROR
#Z[2] = 0 

#----------thing no do with tuples
x = (3, 2, 1)
#x.shor() append reverse incompatibles

# A tbale of TWO Sequences

i= list()
dir(i)

t = tuple()
dir(t)

#---------Tuples are more efficiente

#since python does not have to build tuples strucutures to be 
#modifiable, ther are simpler and more efficient in terms of memmory use and performances than list
#so in our program when we are making "temporary vairbles" 
#we prefer tuples over list   

#.....TUPLES AND ASSIGNAMENT

#WE CAN ALSO PUT A TUPLE ON THE LEFT-HAND SIDE OF AN ASSIGNMENT STATEMENT
#WE CAN EVEN OMIT THE PARENTHESES

(X,Y) = (4, 'FRED')
print(Y)


(a,b) = (99, 98)
print(a)


#---tuples and Dictionaries
#the items() method in dictionaries return a list of (key , value) tuples
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

#---------Tuples are Comparabñe
#THe comparison operator work with tuples and other sequences. if the first item is equal,
#python goes on to the next elements, and so on until it finds elelements that difeer
#with firs elemtn y si son igual se pasa con el 2dalo arguments

print((0,1,2) < (5, 1 , 2))
print(('Jones', 'sally')<('jones','sam'))

print((0, 1, 2000) < (0 , 3 , 4 ))






