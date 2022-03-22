'''Create a class and create its object use constructor and destructor methods within that class'''
class PartyAnimal:
    x = 0
    def __int__(self):
        print("I am constructed")
    def party(self):
        self.x = self.x+1
        print('so far',self.x)
    def __del__(self):
        print('I am destructed',self.x)

an = PartyAnimal()
an.party()
an.party()
an = 65
print('an contains',an)
