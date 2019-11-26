# Example 1
list1 = [x for x in 'AmitPatil']
print("List comprehension example 1:", list1)

# Example 2
list2 = [x**2 for x in range(10)]
print("List comprehension example 2:", list2)

# Example 3 if ---- else
list3 = [x for x in range(0, 10) if x % 2 == 0]
print("List comprehension example 3:", list3)

# Convert Celcious to Fahrenheite
data = [45, 21, 10, 37]
list4 = [((9/5)*temp+32) for temp in data]
print("List comprehension example 4:", list4)

# Nested List Comprehension
list5 = [x**2 for x in [x**2 for x in range(0, 10)]]
print("List comprehension example 5:", list5)
