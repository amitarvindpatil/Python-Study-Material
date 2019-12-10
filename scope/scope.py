# Scope
# A variable is only available inside the region it is created.This is called as Scope

# Local Scope
# A variable declare the inside the function belongs to local scope of the function and can only be used that function


def local_scope():
    # local variable
    x = 30
    print(x + 20)


local_scope()
# o/p= 50

# Function Inside the Function
# local variable access the function inside the function


def outside_funct():
# local variable
    y = 30

    def inside_funct():
        print(y + 10)

    inside_funct()


outside_funct()
# o/p = 40

# Global Scope
# A variable created in main body of the python code is a Global variable and belongs to the Global scope
# global variable are available from within any scope,globals and locals

z = 300


def global_funct():
    print(z + 500)

global_funct()

# o/p = 800
# Naming variables

# If you operate with the same variable name inside and outside of a function
# python treat them as a seprete variable one available in global space and one available in local space

x = 50


def nameing_scope():
    x = 60
    print("Inside value", x)


nameing_scope()
print("glabal value", x)


# Global Keyword
# if you need to create a global variable,but stuck in in the local scope,you can use the global keyword.
# The global keyword make variable global
x = 700


def myfunct():
    global x
    x = 500


myfunct()
print(x)

# o/p = 500