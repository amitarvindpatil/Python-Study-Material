# python date time
# A Date in python it's not data-type of it's own,but we can import a module named datetime to work with dates
# as a date object

# Current date
import datetime
x = datetime.datetime.now()
print("Current Time", x)
print("Year", x.year)
print("Day:-", x.strftime("%A"))

# creating date as object
x = datetime.datetime(2020, 5, 17)
print(x)

# strftime() Method
# A Datetime object has a method for formatting date object into readable string
print("MONTH:-", x.strftime("%B"))
