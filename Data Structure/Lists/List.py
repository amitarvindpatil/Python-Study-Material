# -------------------List------------------------
#  list is a collection which is ordered and changeable. In Python lists are written with square brackets.

# ------Examples-----------
list_data = [10, 'Amit', 'Arvind', 'Patil', 'Sangli']

print("creating List:", list_data)
print("Indexing List:", list_data[1])
# slicing
print("Slicing List1:", list_data[:2])
print("Slicing List2:", list_data[:-2])
print("Slicing List3:", list_data[::2])
print("Slicing List4:", list_data[2:])
print("Slicing List5:", list_data[-2:])
# Make List Double
list_data1 = list_data * 2
print(list_data1)

# -------------------Methods
# length
list_data = [10, 'Amit', 'Arvind', 'Patil', 'Sangli']
print("length Of list:", len(list_data))

#concatinate in List
ls_concat = list_data + ["416416"]
print("Concatinate the list:-", ls_concat)

# append
list_data.append("Maharashtra")
print("Append List:", list_data)

# pop
list_datas = [10, 'Amit', 'Arvind', 'Patil', 'Sangli']
list_datas.pop()
print("Pop List:", list_datas)

# Matrix of Lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
list_matrix = [l1, l2, l3]
print("Matrix of List", list_matrix)

# List Methods
# Length - return a length of list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# append Methods -To add an item to the end of the list, use the append() method:
thislist.append('orange')
print("append method():-",thislist)

# Insert()To add an item at the specified index, use the insert() method:
thislist.insert(1, 'orange')
print("Insert method():-",thislist)

# remove() The remove() method removes the specified item:
thislist.remove('banana')
print("Remove method():-",thislist)

# pop() method The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print("Pop method():-",thislist)

# del keyword - The del keyword removes the specified index:
# you can also del the whole list
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("Del keyword",thislist)

