#  dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
# How To create dictionary
dict_data = {'id': 10, "Name": "Amit Patil",
             "city": "Sangli", "State": "Maharashtra"}

create_new_dict = {}
create_new_dict['id'] = 10
create_new_dict['Name'] = "Vijay"
create_new_dict['City'] = "Sangli"


print("output:-", create_new_dict)

# Accessing the Data
print("Display all dictionary data:-", dict_data)
print("Display perticuler data:-", dict_data['id'])
print("Display perticuler data 2:-", dict_data['Name'])

dict_data1 = {'id': 10, "Name": ["Amit Patil", "vikcy", "mayur"],
              "city": ["Sangli", "Pune", "Mumbai"], "State": "Maharashtra"}

print("Display perticuler from Name:-", dict_data1['Name'][2])
print("Display All data from Name:-", dict_data1['Name'])


# Nesting with Dictionaries
data = {'data1': {"nestdata": {'subnestdata': "Yeeehhhh! GotValue"}}}
value = data['data1']['nestdata']['subnestdata']
print("Display Nested Value:-", value)


# Dictionary Methods
data_items = dict_data1.items()
print("data items:-", data_items)

data_values = dict_data1.values()
print("Represt All values:-", data_values)

data_keys = dict_data1.keys()
print("Represt All keys:-", data_keys)

x = dict_data1.get("Name")
print("get method", x)

# len() method
print("len() method", len(dict_data1))

# copy()
new_dic = dict_data1.copy()
print("Copy() method:-", new_dic)

new_dicw = dict(new_dic)
print("dict() method:-", new_dicw)

# update()
dict_data1.update({'pincode':416416})
print("update() method:-", dict_data1)


# pop()
dict_data1.pop('Name')
print("Pop method():-", dict_data1)

# popitem()
dict_data1.popitem()
print("Popitem method():-", dict_data1)



# using for loop
# for x in dict_data1:
#     print("return the keys only:-", x)

# for x in dict_data1:
#     print("return the value only:-",dict_data1[x])

# # or

# for x in dict_data1.values():
#     print("return the value only:-", x)

# for x,y in dict_data1.items():
#     print("return the item only:-", x,y)
