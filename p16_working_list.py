#--concatenating list using +
#--we can create a new list by adding two existing list together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

#---list can be sliced using:
t = [9,41,12,3,74,15] #declaracion de la lista
print(t[1:3])# inicio - fi
print(t[:4])# inicio en 0 y termino en 4
print(t[3:])# inicio en 3 y termino en -1
print(t[:]) #imprime toda la list

#---List Methods-----------dir and type
x = list()
print(type(x))
print(dir(x))

#-----building a list from scratch
#we can create an empty list and the add alements using the append methos
# the list satay in orden and new elements are added at the end of the list
bulding = list()
bulding.append('Daniel')
bulding.append(205)#numbers is not beds
print(bulding)
bulding.append('aeio')
print(bulding)

#---is something in a list
#python conten operators logics for check a item en the list
#they no modific a list , so only return false or true

some = [1,9,21,10,16]
print(9 in some) #True
print (15 in some) #False 
print (10 not in some) # Falso

#.----- List are in ordee 
friends = ['joseph', 'Glenn', 'Sally']
friends.sort() #ordena los componentes
print(friends) 
print(friends[1]) 

#------ Built-in Function and list 
#function ready existe in pyhthon for 
nums = [2,44,1,3,1,2]
print(max(nums))#  ---max value
print(len(nums))#   ---count items
print(min(nums))#   ---min value
print(sum(nums)/len(nums))#   ---sum all items numerics of list
print(nums)

#------enter numbers of list---
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'stop' :break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average', average)




