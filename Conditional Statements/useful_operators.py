from random import randint
from random import shuffle
# Random Opeator
random_list = [10, 5, 12, 2, 1, 100]
shuffle(random_list)
print("Random Number from shuffle:", random_list)

# Random Integer
x = randint(0, 20)
print(x)

# Range Operator -

x = range(0, 10)
print(x)

# List of Range Operator Same as we can create the tuples and sets
list1 = list(range(0, 10))
list2 = list(range(0, 10, 2))
print("List of Range operator1 -", list1)
print("List of Range operator2 -", list2)

# Enumerator
# Example without Enumerator
i = 1
for ltr in 'amitpatil':

    print("Without Enumerate Index no {} and value is {}".format(i, ltr))
    i += 1

# Example with Enumerator

for i, ltr in enumerate('amitpatil'):
    print("With Enumerate Index no {} and value is {}".format(i, ltr))

# List with Enumerate
ls = list(enumerate('Amitpatil'))
print("List With Enumerate:", ls)

# Zip Operator
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
zip_data = zip(list1, list2)
print(zip_data)
list_zip = list(zip_data)
print("show List data:", list_zip)

for l1, l2 in zip(list1, list2):
    print("list data one :{} list data two :{}".format(l1, l2))

# In operator
in_data = "x" in ['x', 'y', 'z']
print(in_data)

in_data2 = "a" in ['x', 'y', 'z']
print(in_data2)

# MIN and MAX operator
lis = [10, 5, 12, 2, 1, 100]
print("Maximum value from the List:", max(lis))
print("Minimum value from the List:", min(lis))
