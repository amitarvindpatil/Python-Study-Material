# polymorphism
# The Word is polymorphism means having many forms
# In programing langauage Same Function Name but different Data Type

# e.g.
print(len("Amit"))
print(len([0, 1, 2, 3, 4]))


class India:
    def capital(self):
        print("India Capital is DELHI")

    def langauage(self):
        print("Hindi")

    def population(self):
        print("125 cr")


class USA:
    def capital(self):
        print("India Capital is Washington D.C.")

    def langauage(self):
        print("English")

    def population(self):
        print("50 cr")


output_Ind = India()
output_Usa = USA()

for x in (output_Ind, output_Usa):
    x.capital()
    x.langauage()
    x.population()
