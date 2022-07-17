#---list 
#---citccionary 
#A "bag" of values each with own label
#Diccionario de datos con etiqueta is labels 
#Dictionries are python'smost powerfull data collection
#Dictionaries allow us to do fast database-like operations in python
#Dictionaries have different names in different languages
#Asocciate Arrays- Perl/PHP
#Properties or Map or HasMap -Java
#Property Bag -C# /.nET
#

#LIST INDEX THEIR ENTRIES BASED ON THE POSITIOH IN THE LIST
#
#Dictionaries are like bags -no order (not postition?)
#we have do index the dictionary (LOOKUP TAG ---lookup tag)

purse = dict() ##Dicttionary
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

##ccomparing lists and dicttionaries--------

##list 
list = list() # palabra reservada de listas 
list.append(100)
list.append(183)
print(list)
list[0]=213
print(list)

##dictionaries
dic = dict()##palabra reservada diccionario
dic['age'] = 21
dic['curse'] = 65097
print(dic)
dic['edad'] = 2213213
print(dic)

#------Dictionary Literals (Constants)
#Dictionary literals use curly braces and have a list of key: value pairs
#you can make an empty dictionary using empty curly braces

daniel= {'suarez':6, 'nava':4, 'daniel':6}
print(daniel)
ooo = {}
print(ooo) 
