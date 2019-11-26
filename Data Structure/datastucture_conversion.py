
# --------------------------Data Stucture conversion to other--------------------
# String to List
Str_Converion = "Python is one of the massive language Python"

str_list = Str_Converion.split(' ')
print("String To List:", str_list)

# String To List To Tuples
str_list = Str_Converion.split(' ')
Str_tuple = tuple(str_list)
print("String To Tuples:", Str_tuple)

# String To List to Set
str_list = Str_Converion.split(' ')
Str_set = set(str_list)
print("String to Set:", Str_set)

# String To List to Dictionary
str_list = Str_Converion.split(' ')
str_dict = {'str_dict': str_list}
print("To Dictionary:", str_dict)

# Tuples To List
tuple_data = (10, 'Amit', 'Patil', 'Sangli')
tuple_list = list(tuple_data)
print("Tuple To List:", tuple_list)

# Tuples To Sets
tuple_set = set(tuple_data)
print("Tuple To Set:", tuple_set)

# Tuples To Dictionary
tuple_dict = {'tuple_dict': tuple_data}
print("Tuple to Dictionary:", tuple_dict)


# Set To List
Set_data = {10, 'Amit', 'Patil', 'sangli'}
set_list = list(Set_data)
print("Set To List:", set_list)

# Set to Tuple
set_tuple = tuple(Set_data)
print("Set To Tuple:", set_tuple)

# Set to Dictionary
set_dict = {'set_dict': Set_data}
print("Set To Tuple:", set_dict)

# Dictionary To List
dict_data = {"id": 10, "name": "Amit", "city": "sangli"}
dict_list = list(dict_data.values())
print("Dictionary to List", dict_list)

dict_data1 = {"id": 10, "name": "['Amit','Arvind']", "city": "sangli"}
dict_listss = list(dict_data1.values())
print("Dictionary to List", dict_listss)
