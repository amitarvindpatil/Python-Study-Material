# lambda is an Anonymous Function
# Anonymous Function means a "Function Without Name"
# lambda doesn't include the return Statement
# This Function can have any number of argument but return only one expression

# Syntax : lambda arguments:expression

# Example of normal Function


from functools import reduce


def cube(no):
    return no*no*no


print(cube(7))

# Example of Lambda Function


def g(x): return x*x*x


print(g(7))


def a(x): return x+20


print(a(50))


def c(x, y): return x+y


print(c(10, 20))

# use lambda function is defination


def myfunct(n):
    return lambda a: a * n


mytripler = myfunct(5)
print("lambda in defination:-", mytripler(5))

# fibbonaci in lambda function
fib = lambda n :reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2),[0,1])
print("Fibbonacci series",fib(5))

# Example of Lambda with filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)


# Example of Lambda with MAP
lis = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list1 = list(map(lambda x: x * 2, lis))
print(final_list1)
