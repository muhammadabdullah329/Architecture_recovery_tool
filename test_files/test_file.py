class Person:
    x[3] = {1,7,54}
    d = 3

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        d = 3+1
        print(self.firstname, self.lastname)


class Student(Person):
    d = 3
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

if class is true:
    pass

def printfunc():
    print("abc = 3")
#this is a comment
x = Student("Mike", "Olsen", 2019)
x.welcome()

class Test:
    test_variable = 2

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def testFunction(self):
        print(self.firstname, self.lastname)


class homework(Student):
    hw = "srw"
    cw = "sdw"

    def myfunction ():
        print("sadasf")
