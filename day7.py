# Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
# print(thisdict["year"])
# print(len(thisdict))


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type

thisdict= {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


# The dict() Constructor
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)


# Python - Access Dictionary Items
# print(thisdict["brand"])
# x = thisdict["electric"]
# x = thisdict.get("electric")
# print(x)


# Get Keys
# x = thisdict.keys()
# x = thisdict.keys();
# print(x)    

# thisdict["model"] = "mustang"
# print(x)



# Get Values

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# x = car.values()
# print(x)
# car["year"] = 2020
# car["color"] = "red"
# print(x) #after the change


# Get Items
# x = car.items();
# print(x)
# car["color"] = "red"
# print(x)


# Check if Key Exists
# if "brand" in car:
#     print("yes")


# Python - Change Dictionary Items
# car ["year"] = 2020
# car.update({"year" : 2024})
# print(car)


# Python - Remove Dictionary Items
# car.pop("year")
# car.popitem()
# del car["model"]
# del car
# car.clear()
# print(car)


# Python - Loop Dictionaries
# for x in car:
#     print(x)

# for x in car.keys():
#     print(x)

# for x in car.values():
#     print(x)

# for x, y in car.items():
#     print(x, y)

# copy dictionaries
# x = car.copy();
# x = dict(car)
# print(x)


# Python - Nested Dictionaries -> A dictionary can contain dictionaries,  called nested dictionaries.
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

child1 = {
    "name" : "Emil",
    "year" : 2004
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

child3 = {
   "name" : "Linus",
    "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# print(myfamily)


# Access Items in Nested Dictionaries
# print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

for y in obj:
    print(y + ':', obj[y])