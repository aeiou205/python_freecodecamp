#-----------A list is a find of Collection--------
friend = [ 'daniel' , 'Glenn', 'Sally' ]
carryon = [ 'socks' , 'shirt', 'perfume']
print(friend)
#------list constans-----------------
print([1, 24, 76])
print(['read', 'yellow', 'blue'])
print([1, [5, 6], 7])
print([])
#------we already use list----------
for i in [5,4,3,2,1] :
    print([i])
print('aeiou')
#----list and definite loops - best pals

for friend in friend :
    print('buen dia' , friend)
print('DOne!')


z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print("happy new york;",x)
print("DONE")

#------lOOKING INSIDE LIST
firends = ['josep', 'Gleen', 'sally']
print(firends[1])
#------List are Mutable
fruit = 'banan'#VCON STRING NO PUEDES CAMBIAR VALORES 
#fruit[0] = 'x'<----------- NO SE PUEDE
x = fruit.lower()
print(x)
lotto = [2,14,12,14,43]
lotto[2] = 28
print (lotto)
#------how long is a list?----------
greet = "hello bob"
print (len(greet))
x = [1, 2, 'joe', 99]
print(len(x))

#----Using the range function--------
print(range(4)) #FUNCTION RANGE RETURNS A LIST OF NUMBERS THAT RANGE FROM ZERO TO ONE LESS THAN THE PARAMETER
print(len(firends)) #LEN FUNCTION TAKES A LIST A PARAMETER AND RETURNS THE NUMBER OF ELEMENTS IN THE LIST

#-- A LATE OF TWO LOOPS--------
print(len(firends))
print(range(len(firends)))

