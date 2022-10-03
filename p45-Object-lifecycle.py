#Object lifeycle
#Objects are created, used and discarded
#we have special blocks of code (methods) that get called
#at the moment of creation (constructor)
#at the moment of destruction(destructor)
#constructor are used a lot
#Destructor are seldom used

class PartyAnimals:
    x = 0
    def __init__(self):
        print('I am constructed')
    
    def party(self):
        self.x = self.x + 1
        print('so far' , self.x)
    
    def __del__(self):
        print('i am destructed ', self.x)
    
an = PartyAnimals()
an.party()
an.party()
an = 42
print('an contsind', an)

#The constructor is de bloque especial de codigo que se llama cuando se configurar el objeto 

#Many instances

#We can create lots of objects - the class is the template for the object

# We can store each distinct objects in its own variable

# we call this having multiple instances of the same class

# Each instances has its own copy of the instance variables 

class PartyAnimal:
    name = ""
    x = 0
    def __init__(self,z):
        self.name = z
        print(self.name,"constructed")
    
    def party(self):
        self.x  = self.x + 1
        print(self.name,"Party count",self.x)

s = PartyAnimal('sally')
s.party()

j = PartyAnimal("jim")

j.party()
s.party()


