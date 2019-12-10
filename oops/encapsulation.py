# Encapsulation
# Using OOP in Python, we can restrict access to methods and variables.
# This prevent data from direct modification which is called encapsulation.
#  In Python, we denote private attribute using underscore as prefix
# i.e single “ _ “ or double “ __“.


class Computer:
    def __init__(self):
        self.__maxprice = 5000

    def sale(self):
        print("Saleing price is : {}".format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price


c = Computer()
c.sale()

c.__maxprice = 10000
c.sale()

c.setMaxprice(10000)
c.sale()
