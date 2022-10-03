"""
when we make a new class - we can reuse an existing class and inherit all the capabilities 
of an existing class  and add our own little bit to make our new class

Another form of store and reuse

write once - reuse many times 

the new class (child ) has all the capabilities of the old
class(parent) -- and then some more


"""
class PartyAnimal:
    name = ""
    x = 0
    def __init__(self,z):
        self.name = z
        print(self.name,"constructed")
    
    def party(self):
        self.x  = self.x + 1
        print(self.name,"Party count",self.x)



class FootbaallFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.point = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal('sall')
s.party()

j = FootbaallFan('jim')
j.party()
j.touchdown()
