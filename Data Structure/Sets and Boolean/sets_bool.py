# Sets data elements are uniquely represent in unorder data.
# set is a collection which is unorder and unindexed.
# Mention in {}
# Creating Sets
data_set = [1, 10, 10, 2, 3, 4, 4, 5, 1]
data = set(data_set)
print("creating sets", data)

# how to access sets
for x in data:
    print(x)

x = set()
x.add(1)
x.add(2)
print(x)

# methods
# len()
print("len() method:-", len(data))
# remove() and discard()  To remove an item in a set, use the remove()
data.remove(10)
print("remove method", data)

# pop() method Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
data.pop()
print("pop method", data)

# clear()
da = {1, 2, 3, 4, 5, 6, 7}
da.clear()
print("clear() method:-", da)

# del key
# da = {1, 2, 3, 4, 5, 6, 7}
# del da
# print("del keyword", da)

# Join Two Sets
# union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("using union() method:-", set3)

# update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print("using update() method:-", set1)

# copy()
x = set1.copy()
print("using copy() method:-", x)


# Boolean
z = True
print(z)

# none placeholder
c = "None"
print(c)
