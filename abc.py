class Person:
    def __init__(self, name, age, div):
        self.name = name
        self.age = age
        self.div = div

    def printdata(self):
        print(self.name, self.age, self.div)
# CHILD class


class Student(Person):
    def printdatas(self):
        print(self.div)


op = Student("Amit", 25, "A")
print(op.printdata())
print(op.printdatas())
