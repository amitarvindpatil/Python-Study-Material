# --------------Map Built in Functions
# The map function allows you to "map" a function to an iterable object.
#  That is to say you can quickly call the same function to every item in an iterable, such as a list

# Example -1


def squre(num):
    return num ** 2


my_num = [1, 2, 3, 4, 5]
output_list = map(squre, my_num)
print("Map Example first output:", list(output_list))

#Example -2


def validation(Names):
    if Names[0] == 'A':
        return "Permission Granted To " + Names

    else:
        return "Permission Granted To " + Names


Names = ["Amit", "Arvind", "prasad"]
validation_list = map(validation, Names)
print(list(validation_list))


# Example 3
def splicer(oddeven):
    if len(oddeven) % 2 == 0:
        return 'even'
    else:
        return 'odd'


oddeven = ["Amit", "Arvind", "prasada"]
oddeven_op = map(splicer, oddeven)
print(list(oddeven_op))
