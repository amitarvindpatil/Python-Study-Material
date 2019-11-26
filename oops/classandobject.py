# Class
# python is an object oriented programing language
# class is the collection methods,attributes and properties
# object - object is an istance of a class


class Test:
    x = 5


p1 = Test()
print(p1.x)

# in above property Test is class name and x is property, p1 is an "object" and print value of x

# __init()__ fuction
# This is a built-in function
# all classes have function __init__(), which is always executed when the class is being Initiated
# use of __init__() function to assign a value to object properties.

# example
# Note - The __init__() function is called automatically everytime the class is being used to create a new object


class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p2 = TestClass("Amit", 26)
print(p2.name)
print(p2.age)

# object Method


class Student:
    def __init__(self, fname, std):
        self.fname = fname
        self.std = std

    def view(self):
        print("Name of student  "+self.fname)
        print("Standard of student", self.std)


p = Student("Rohit", 26)
print(p.view())

# The Self parameter
# The self parameter is a reference to current instance of a class and is used to access variable
# that belongs to the class
# It is not compulsory declare name as self,we can use different name


class Person:
    def __init__(data, name, age):
        data.name = name
        data.age = age

    def tests(dat):
        print("Hellow my name is" + dat.name)
        print("Hellow my name is", dat.age)


da = Person("Amit", 50)

print(da.tests())

# modify the object properties

da.age = 40
print(da.tests())

# Delete Object Properties
# del da.age
# print(da.tests())
