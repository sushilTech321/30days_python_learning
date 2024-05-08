# Python Dates
# A date in Python is not a data type of its own,
# but we can import a module named datetime to work with dates as date objects

import datetime

x = datetime.datetime.now()
# print(x)
# print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%w"))
print("Day of month,",x.strftime("%d"))
print("Month name, short version:",x.strftime("%b"))
print("Month name, full version:",x.strftime("%B"))
print("Month as a number :",x.strftime("%m"))
print(x.strftime("%Z"))

print()

# Creating Date Objects

# x = datetime.datetime(2020, 5, 12)
# print(x)
# print(x.strftime("%A"))
# print(x.strftime("%B"))



# Python Math
print("Python Math")

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x) #return 5
print(y)    #return 25

x = abs(-7.25)

print(x)    # return 7.25

x = pow(4, 3)

print(x)  #return 64


# The Math Module
import math
x = math.sqrt(25)

print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

x = math.pi
print(x)