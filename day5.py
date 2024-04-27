# Loop Through a List
thislist = ["apple", "banana", "cherry","watermelon","mango","cherry"]
# for x in thislist:
#   print(x)


# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
thislist = ["car", "bus", "bike","van","taxi","truck"]
# for i in range(len(thislist)):
#   print(thislist[i])


# Using a While Loop, use len() function to determine the length of the list, then start at 0 and 
# loop your way through the list items by referring to their indexes.
thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
# [print(a) for a in thislist]


# List Comprehension ->  it offers a shorter syntax
# Example: Based on a list of fruits, want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# With list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "e" in x]
# newlist = [x for x in fruits if x!="kiwi" and x!= "mango"]
# newlist = [x for x in fruits]
# newlist = [x for x in range(10)]      #use the range()
# newlist = [x for x in range(10) if x <= 5]    #with a condition:
# newlist = [x.upper() for x in fruits]        #new list to upper case:
# newlist = [x if x != "banana" else "orange" for x in fruits]       # Return "orange" instead of "banana":
# print(newlist)


# The Syntax
# newlist = [expression for item in iterable if condition == True]

