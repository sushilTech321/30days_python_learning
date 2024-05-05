# Python JSON

import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# print(y)
# print(y["age"])


x = {
    "name" : "jack",
    "age" : 39,
    "post" : "developer"
}

y = json.dumps(x)
# print(y)

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# Python RegEx

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# if x:
#      print("YES! We have a match!")
# else:
#   print("No match")


# Python Try Except


# Many Exceptions
# try:
#   print(a)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# Else
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


#  Finally
# try:
#   print(s)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


#   Raise an exception
# e = -1

# if e < 0:
#   raise Exception("Sorry, no numbers below zero")

