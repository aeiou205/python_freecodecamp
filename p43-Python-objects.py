
#Thsi lecture is very much about definitions and machanics for object

#This lecture is a lot more about "how it works" and less about" how you use it

#You won't get the entire picture until eso es mirado en el contexto de un problema real

#so please suspend disbelief and learn technique for the next 50 or so slides.



from sympy import together


inp = input('Europe floor?')
usf = int(inp) + 1 
print('US floor', usf)

#A program is made up of many cooperating objects

#Instead of being the whole program - each object is a little island within the program and
#cooperativelty working with other objects

#A program is made up of one or more objects working
#together - objects make use of each others capabilites

# An object is a bit of - self- contained code and data
#A key aspect of the object approach parts (divide and conquer)

#OBject have boundaries thath allow us to ignore un-needed datail integer objects, Dictionary 
#Objects, List Object

#definitions
"""
#Definitions

#Class - a template - Dog 
#Method or Message - A defined capability of a class - bark ()
FIeld or attribute - A bit of data in a class - length
Object or instance - A particular instance of a classs - lassie

"""

#the cookie box is example about class for object
#objects are cookies