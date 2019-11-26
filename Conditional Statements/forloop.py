# For looping statements

# Example-1 Odd Even Programs
list_data = [10, 11, 12, 13, 14, 15, 16]
for data in list_data:
    if data % 2 == 0:
        print("even Numbers:-", data)
    else:
        print("odd Numbers:-", data)


# Example -2 For Loop with Nested List
x = ['x', 'y', 'z']
a = ['a', 'b', 'c']
for xy in x:
    for sb in a:
        print(xy, sb)

# Example -3 For loop list of tuples
list1 = [(1, 2), (3, 4), (5, 6)]
for ls in list1:
    print(ls)

# unpacking the List of Tuples
for l1, l2 in list1:
    print(l1, l2)

# ForLoop with Dictionaries
dict_data = {
    'id': 10,
    'Name': 'Amit',
    'city': ['Sangli', 'Pune'],
    'isActive': True
}
for k1 in dict_data.items():
    print("show all items:-", k1)

for k2 in dict_data.values():
    print("show all values:-", k2)

for k3 in dict_data.keys():
    print("show all values:-", k3)


# For loop with Function
