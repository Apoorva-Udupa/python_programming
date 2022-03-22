# task: to create mutliple instance of a class
class Record:
    name = ''
    roll_no = 0
    def __init__(self,z,r):
        self.name = z
        self.roll_no = r
        print("I am constructed")

    def disp(self):
        print("Name of the student = ",self.name)
        print("Roll No = ",self.roll_no)

    def __del__(self):
        print("I am destructed",self.roll_no)

name1 = Record('Sara',1)
name2 = Record('Jay',2)
name2.disp()
name2 = 'jaya'
print(name2)
name1.disp()
