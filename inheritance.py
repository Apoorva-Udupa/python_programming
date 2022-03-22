'''use inheritance property for Animals example'''
class Animal:
    name = ''
    legs = 0
    def __init__(self,n,l):
        print("Animal Created")
        self.name = n
        self.legs = l
    def walk(self):
        print("{} is walking with {} legs".format(self.name,self.legs))
class Mammal(Animal):
    ebones = 0
    def characteristics(self):
        self.walk()
        self.ebones = 2
        print('I have {} earbones'.format(self.ebones))
        print('Name is ',self.name,'and has ',self.legs,' legs and ear bones are',self.ebones)

s = Mammal('cow',4)
k = Animal('owl',2)
s.characteristics()
k.walk()
