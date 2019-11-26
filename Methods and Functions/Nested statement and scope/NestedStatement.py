# Nested Statement And Scope
# python deals with variables name you assign.When you create variable name in python the name is stored
# in name-space.Variable name also have scope. The determine the visibilty of scope

# Example
x = 25

def printer():
    x = 50
    return x


print(x)
print(printer())

# The SCOPE can be describe into 3 general Rules
# 1. Name of the assignments will create or change local names by default
# 2. Name refernce search four scope
# -local
# -enclosing Function
# -global
# -built-in
# 3. The Names declared in global and nonlocal statements map assigned names to enclosing modules and Function scope

# LEGB Rules
# -Local - Name assign with in the Function


def f(x):
    return x**2


f(5)

# - Enclosed Function Local
# Name in the local scope of any and all enclosing functions(def/lambda) from inner to outer
name = "This is global Name"


def greet():
    # Enclosing Function
    name = "Sammy"

    def hello():
        print('Hello' + name)

    hello()


greet()
# Global- Name assign to top-of the module file,or declare with in the def
print(name)
x = 50


def glob_funct():
    global x
    print("This Function is now using the global x!")
    print("Beacuse of the x is:", x)
    x = 2
    print("Ran funct() changed global x to", x)


print("Before calling Funct(), x is:", x)
glob_funct()
print("value of x outside the function", x)

# Built-In -Names Pre-assigned in the built-names modules: open,range
print(len('Amit'))
