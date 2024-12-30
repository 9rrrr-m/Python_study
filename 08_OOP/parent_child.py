class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")


x = Person("Harry", "Potter")
x.printname()

y = Student("Hermione", "Granger", 2020)
y.printname()
print(y.firstname)
print(y.graduationyear)
y.welcome()
