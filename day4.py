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


# Python - Sort Lists
# Sort List Alphanumerically -> sort() method that will sort the list alphanumerically, ascending, by default

thislist = ["Orange", "mango", "apple", "kiwi", "pineapple", "Banana"]
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()         
# thislist.sort(reverse = True)  # Sort Descending
# thislist.sort(key = str.lower)         
# thislist.reverse()
# print(thislist)


# Python - Copy Lists
country_list = ["India", "United States", "China", "United Kingdom", "Brazil", "Russia", "Japan", "Germany", "France", "South Korea"]
# copylist = country_list.copy()
# copylist = list(country_list)
# print(copylist)
# x = country_list.count("India")
# x = country_list.index("China")
# print(x)

# Python - Join Lists
list1 = ["1","2","3"]
list2 = ["a","b","c",]
# slist = list1+list2  # method 1
# print(slist)
# for x in list2:
#     list1.append(x)       # method 2
# print(list1)

# list1.extend(list2)     # method 3
# print(list1)