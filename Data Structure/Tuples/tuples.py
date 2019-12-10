# Tuples Creation
# Tuples are collection of iterables which order and unchangables
# Note - Tuple are immutuability - we cannot do append,pop and modify the tuples

tuple_data = (10, "Amit", "Arvind", "patil")
print("tuple data set:-", tuple_data)

# Slicing Of Tuples
print("Slicing of tuples1:-", tuple_data[:2])
print("Slicing of tuples2:-", tuple_data[::2])
print("Slicing of tuples3:-", tuple_data[:-2])
print("Slicing of tuples4:-", tuple_data[2:])
print("Slicing of tuples5:-", tuple_data[-2:])
print("Slicing of tuples6:-", tuple_data[-2])

# Tuples Methods
# index
x = tuple_data.index('Amit')
print("Index postion:-", x)

tuple_count = tuple_data.count(10)
print("Tuple Count:", tuple_count)

# how to modify the tuples
data = (10, 20, 30)
x = list(data)
x[1] = "AA"
tup = tuple(x)
print(tup)


# Immutuabiltiy
# tuple_data[1] = "Abc"
# print(tuple_data)

# tuple_data.append("xyz")
# print(tuple_data)
