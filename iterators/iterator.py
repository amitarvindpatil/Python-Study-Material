# Iterator
# An Iterator is an object that contains a countable number of values
# An  Iterator is an object that can be iterated upon,meaning that you can traverse throught all the value
# Technically in python, an Iterator is an object which implements the Iterator protocal, which consists of the methods
# __iter__() and __next__()

# iterator vs iterable
# List, tuples, dictionaries and sets all are iterable object.They are iterable containers
# which you can get an iterator from

# iter() method
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)


# Create an iterator
# To Create an object/class as an  iterator you have to implements the methods __iter__() and __next__() to your object
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows
#  you do some initializing when the object is being created.

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

# The __next__() method also allows you to do operations, and must return the next item in the sequence.

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):s

class Mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = Mynumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.

class Mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = Mynumber()
itrrs = iter(myclass)

for x in itrrs:
    print(x)
