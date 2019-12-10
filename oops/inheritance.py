# Inheritance
# Inheritance allow us to define a class that inherits all properties and method from anather class
# Parent class is the class being inherited from,also called as Base Class
# child class is that inherits from another class, also called derived class

# parent class


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


# use init() method
class Student(Person):
    def __init__(self, name, age, div):
        Person.__init__(name, age, div)


# op = Student("sallu", 25, "B")
# print(op.printdata())


# super() function that child class inherit all properties and methods from parent class
# add properties in base class
class Student(Person):
    def __init__(self, name, age, div, rollno):
        super().__init__(name, age, div)
        self.rollno = rollno

    def printdatas(self):
        print(self.name, self.age, self.div, self.rollno)


# Multilevel Inheritance


class Subject(Student):
    def __init__(self, name, age, div, rollno, marks):
        super().__init__(name, age, div, rollno)
        self.marks = marks

    def printdatas(self):
        print(self.name, self.age, self.div, self.rollno, self.marks)


op = Subject("rahul", 28, "B", 50, 64)
print(op.printdatas())

# # Multiple Inheritance


class Arvind:
    def __init__(self, asset, sqft, price):
        self.asset = asset
        self.sqft = sqft
        self.price = price


class Anita:
    def __init__(self, Metal, kg):
        self.Metal = Metal
        self.kg = kg


class Amit(Arvind, Anita):
    def __init__(self, asset, sqft, price, Metal, kg, flat):
        Arvind.__init__(self, asset, sqft, price)
        Anita.__init__(self, Metal, kg)
        self.flat = flat

    def showproperty(self):
        print(self.asset, self.sqft, self.price,
              self.Metal, self.kg, self.flat)


output = Amit('Land', 30000, '5CR', 'Gold', '5', '2BHK')
print(output.showproperty())
