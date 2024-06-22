"""
    Python Tuples
    1. A tuple is a collection which is ordered and unchangeable and allow duplicates.
    2. Tuples are written with round brackets.
"""
thistuple = ("apple", "banana", "cherry","grapes","watermelon")
# thistuple = tuple(("apple", "banana", "cherry", 1, 3, True))
# thistuple = ("apple",)
# print(thistuple)
# print(len(thistuple))
# print(type(thistuple))


# Python - Access Tuple Items
# print(thistuple[2])
# print(thistuple[-2])
# print(thistuple[2:5])
# print(thistuple[2:])
# print(thistuple[-4:-1])

#check if exits item
# if ("apple" in thistuple):
#     print("Yes")
# else:
#     print("No")


# Python - Update Tuples
# convert the tuple into a list, change the list, and convert the list back into a tuple.

# mytuple = list(thistuple)
# mytuple[0] = "mango"
# mytuple.insert(2,"mango")
# mytuple.append("blackberry")
# thistuple = tuple(mytuple)
# print(mytuple)
# print(thistuple)


# Remove Items
# mytuple = list(thistuple)
# mytuple.remove("watermelon")
# mytuple.pop()
# mytuple.clear()
# del mytuple
# print(mytuple)

# thistuple = tuple(mytuple)
# print(thistuple)


# Python - Unpack Tuples
(green, yellow, red, blue, gray) = thistuple
# print(green)
# print(yellow)
# print(red)
# print(blue)
# print(gray)

# Using Asterisk*
# (green, *yellow, red) = thistuple
# print(green)
# print(yellow)
# print(red)


# Python - Loop Tuples
# for x in thistuple:
#     print(x)

# for x in range(len(thistuple)):
#     print(thistuple[x])

# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i += 1


tuple1 = ("a","b","c","a")
tuple2 = (1,2,3)
# tuple3 = tuple1 + tuple2
# tuple3 = tuple1 * 4
# tuple3 = tuple1.count("a")
tuple3 = tuple1.index("a")
print(tuple3)