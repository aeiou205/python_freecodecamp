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







