# Variable assign Small program
p = 500
n = 10
r = 20
Simple_Interest = (p*n*r)/100
print("Simple Interest:", Simple_Interest)

# Compoud interest
time = 2
power = n * time
CI = p + (1 + n/r) ** power
print("Compund Interest:", CI)

# ----------------String Operations-------------------------
# Description -
# strings in Python are arrays of bytes representing unicode characters. However,
# Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string

string = "Python is one of the massive language 50"
print("String Creation:", string)
print("String indexing:", string[0])
# Slice
Slice_String = "Hellow"
print("String Slice1:", Slice_String[:3])
print("String Slice2:", Slice_String[:-2])
print("String Slice3:", Slice_String[::2])
print("String Slice4:", Slice_String[2:])
print("String Slice4:", Slice_String[-2:])

# Methods
Methods_String = "Hellow"
print("Length of string:", len(Methods_String))

Methods_String = Methods_String + " Python"
print("Concatination:", Methods_String)

# upper()
print("Upper method:", Methods_String.upper())

# lower()
print("Lower method:", Methods_String.lower())

# Split
splits = Methods_String.split(' ')
print("Split String :", splits)


# join()	Joins the elements of an iterable to the end of the string
mytuple = ("A", "B", "c")
op = "#".join(mytuple)
print("join()", op)

# count() Returns the number of times a specified value occurs in a string

op = string.count('a')
print("Count Method output:-", op)

# find() Searches the string for a specified value and returns the position of where it was found

sa = string.find("massive")
print("Find method:-", sa)

# index() 	Searches the string for a specified value and returns the position of where it was found
sa = string.index("massive")
print("Index method:-", sa)

# islower()	Returns True if all characters in the string are lower case
op = data.islower()
print("islower method:", op)

# isupper()	Returns True if all characters in the string are upper case
data = "HELLO"
op = data.isupper()
print("isupper() method:", op)


# ljust()	Returns a left justified version of the string
data = "banana"
op = data.ljust(20)
print("ljust() method:", op)

# lstrip()	Returns a left trim version of the string
data = "          banana         "
op = data.lstrip()
print("lstrip() method:", op)

# strip() Remove spaces at the beginning and at the end of the string:
data = "    banana    "
op = data.strip()
print("strip() method:-", op)

# isspace()	Returns True if all characters in the string are whitespaces
data = "   "
op = data.isspace()
print("isspace() method:", op)

# other Methods

# check value of present in string
op = " " in Methods_String
print("Check value in:-", op)


# casefold() Converts string into lower case
op = lang.casefold()
print("CaseFold method:", op)

# center()	Returns a centered string
op = lang.center(50, 'O')
print("center method:", op)


# encode() method Returns an encoded version of the string
val = "My Name is Amit."
op = val.encode(encoding="ascii", errors="backslashreplace")
print("encode Method output:-", op)

# endswith()	Returns true if the string ends with the specified value Returns True or False
op = val.endswith('.')
print("endswith() Method output:-", op)

# expandtabs()	Sets the tab size of the string
valv = "H\te\tl\tl\to"
x = valv.expandtabs(2)
print(x)


#  isalnum() Returns True if all characters in the string are alphanumeric
val = "AmitP"
sa = val.isalnum()
print("isalnum method:-", sa)

# isalpha() Returns True if all characters in the string are in the alphabet
sa = val.isalpha()
print("isalpha method:", sa)

# isdecimal()	Returns True if all characters in the string are decimals
data = "\u0033"
sa = data.isdecimal()
print("isdecimal method:", sa)

# isdigit()	Returns True if all characters in the string are digits
data = "10000"
op = data.isdigit()
print("isdigit method:", op)

# isidentifier()	Returns True if the string is an identifier
data = "omya"
op = data.isidentifier()
print("isidentifier method:", op)


# isnumeric()	Returns True if all characters in the string are numeric
data = "1234"
op = data.isnumeric()
print("isnumeric method:", op)

data = "Hello! Are you #1?"
op = data.isprintable()
print("isprintable method:", op)


# istitle()	Returns True if the string follows the rules of a title
data = "Hello, And Welcome To My World!"
op = data.istitle()
print("istitle() method:", op)



# maketrans()	Returns a translation table to be used in translations
dicti = {"a": 123, "b": 465, "c": 789}
string = "abc"
print("maketrans() method", string.maketrans(dicti))

# partition()	Returns a tuple where the string is parted into three parts
data = "I could eat bananas all day"
op = data.partition("eat")
print("partition() methods", op)

# rfind() Searches the string for a specified value and returns the last position of where it was found
data = "I could eat bananas all day eat"
op = data.rfind("eat")
print("rfind() methods", op)

# rindex()	Searches the string for a specified value and returns the last position of where it was found

op = data.rindex("eat")
print(op, "rindex() methods")

# rjust()	Returns a right justified version of the string
# Return a 20 characters long, right justified version of the word "banana":
data = "banana"
op = data.rjust(20)
print(op, "rjust() methods")

# rpartition()	Returns a tuple where the string is parted into three parts
data = "I could eat bananas all day, bananas are my favorite fruit"
op = data.rpartition("bananas")
print("rpartition() methods:-", op)

# rsplit()	Splits the string at the specified separator, and returns a list
string = "apple, banana, cherry"
op = string.rsplit(",")
print("rsplit() methods:-", op)

# rstrip() Remove spaces to the right of the string:
data = "    bananas     "
op = data.rstrip()
print("rstrip() method output:-of all fruits", op, "is my favorite")

# splitlines()	Splits the string at line breaks and returns a list
data = "Thank you for the music\nWelcome to the jungle"
op = data.splitlines()
print("splitlines() method :-", op)

#  startswith()	Returns true if the string starts with the specified value
data = "Hello, welcome to my world."
op = data.startswith("Hello")
print("startwith() method:-", op)



# swapcase()	Swaps cases, lower case becomes upper case and vice versa
data = "BaNaNa"
op = data.swapcase()
print("swapcase()Method:-", op)

# title()	Converts the first character of each word to upper case
data = "hi i am amit"
op = data.title()
print("Title() Method:", op)

# zfill() Fill the string with zeros until it is 10 characters long:
data = "50"
op = data.zfill(10)
print("zfill() Method:-", op)

# Escape character
txt = "We are the so-called \"Vikings\" from the north."
txts = "Esacpe character \\Vikings (Backslash)."
txt1 = "Esacpe character \n (New Line)."
txt2 = "Esacpe character\r(Carriage return)."
txt3 = "Esacpe character\t(Tab)."
txt4 = "Esacpe character\b(BackSpace)."
txt5 = "Esacpe character\f(FormFeed)."
txt6 = "\110\145\154\154\157"
txt7 = "\x48\x65\x6c\x6c\x6f"
print(txt)
print(txts)
print(txt1)
print(txt2)
print(txt3)
print(txt4)
print(txt5)
print(txt6)
print(txt7)
