# Python Conditions and If statements
a = 33
b = 200
# if b > a:
#     print("b is greater than a")

# if (a == b):
#     print("a and b are equal number")
# elif (a > b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")


# Short Hand If
# This technique is known as Ternary Operators, or Conditional Expressions.
# if b > a : print("b is greater than a")
# print("a") if a > b else print("b")


# And logical operator 
a = 0
b = 2
c = 3
# if a > b and c < b:
#   print("both condition are true")
# else:
#   print("both condition are false")

# or operator
# if a < b or c < b:
#   print("both condition are true")
# else:
#   print("both condition are false")

# not operator
# if not a > b:
#     print("a  less than b")


# Nested if 
x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

# The while Loop
i = 0
# while i < 6:
#   print(i)
#   if( i > 3):
#     break  #break statement
#   i += 1


# The continue Statement
# while i < 10 : 
#     i += 1
#     if (i == 4):
#         continue
#     print(i)
# else:
#     print("i is no longer less than 10")


# Loop statement
# thislist = ["stress", "relief", "anxiety", "depression", "motivation"]
# for x in thislist:
#     # print(x)
#     if x == "relief":
#         # break
#         continue
#     print(x)


# for y in range(2, 10):
#     print(y)

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)