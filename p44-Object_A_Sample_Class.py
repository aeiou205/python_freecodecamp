# A sample Class
#una instancia de uan clase

class PartyAnimal:
    x = 0
    x2 = 0
    def party(self):
        self.x = self.x + 1
        print("so far",self.x)

    def playing_dir_and_type(self):
        self.x2 = list()
        type(self.x2)
        print(dir(self.x2))





an = PartyAnimal()

print(type(an))
print(dir(an))


