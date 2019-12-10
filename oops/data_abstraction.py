# data abstraction
# abstration means hiding the complexity and showing the essential feature of the object
# means hiding the real implimentation and we,as user knowing how to use it


# example
from abc import ABC, abstractclassmethod


class Polygon(ABC):
    # Abstract Method
    def noofsides(self):
        pass


class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")


class Squre(Polygon):
    def noofsides(self):
        print("I have 4 sides")


class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")


R = Triangle()
R.noofsides()

S = Squre()
S.noofsides()

H = Hexagon()
H.noofsides()
