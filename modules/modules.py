# Modules
# consider a module to be same as a code library
# A file containing a set of functions you want to include in your  application

# create a module in a.py
import platform
import a
from b import student

a.greetings("Amit")
b = a.person['age']
print(b)

# Built-in
x = platform.system()
print(x)

# using dir function
x = dir(platform)
print(x)


# Import from module
print(student["age"])
