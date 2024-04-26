# Python - Add List Items
# Append Items -> append() method, To add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Insert Items -> insert() method, insert a list item at a specified index,
thislist1 = ["car", "bus", "van","motorbike"]
thislist1.insert(2, "bycycle")
print(thislist1)


# Extend List -> extend() method, append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add Any Iterable, Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

