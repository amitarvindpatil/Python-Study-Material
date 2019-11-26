# Methods
# 1 - append- add value at end of the list
# 2 - count - retrive the count of passing value
# 3 - extend - add multiple element in the list
# 4 - insert - insert element at perticuler position
# 5 - pop - Remove Last value
# 6 - remove - Remove perticuler value
# 7 - reverse - reverse the whole array/List
# 8 - sort - Sort list in sequences

list1 = [1, 2, 2, 'amit', True, 4.5]
list1.append("patil")
print("Append Method", list1)

lcount = list1.count(2)
print("Count method", lcount)

list1.extend(['A', 5])
print("Extend Method", list1)

list1.insert(1, 'paap')
print("Insert Method:", list1)

list1.pop()
print("Pop Method:", list1)

list1.remove('paap')
print("Remove Method:", list1)

# list1.remove('paap')
print("Remove Method:", list1)

list2 = [10, 20, 30, 40, 50, 40]
list2.sort()
print("sort Method:", list2)
