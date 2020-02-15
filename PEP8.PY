#Program to show use of constuctor and destructor
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def getFullName(self):
        print(fname,lname)

    def __del__(self):
        print("Destroying instance of person class")

p1=Person("Emraan","Hashmi")
p1.getFullName()
p2=Person("Rohit","Sharma")
p2.getFullName()
#p1 None
#p2 None
p1.__del__()
p2.__del__()


              
