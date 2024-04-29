# Python Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are unordered, so you cannot be sure in which order the items will appear.

thisset = {"fish","goat","whale","tiger"}
# thisset = set(("fish","goat","whale","tiger"))    #creating set using set() constructor
# print(thisset)
# print(type(thisset))
# print(len(thisset))

# for x in thisset:
#     print (x)

# if "fish" in thisset:
#     print("yes")

# print("fish" not in thisset)


# Python - Add Set Items
# x = list(thisset)
# x.append("mango")
# thisset = set(x)
# print(thisset)
# print(type(x))

# thisset.add("lion")
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)


# Add Any Iterable
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)


# Python - Remove Set Items
remset = {"apple", "banana", "orange", "grape", "kiwi"}
# remset.remove("apple")
#remset.discard("grape")
# remset.pop()
# remset.clear()
# del remset
# print(remset)

set1 = {"apple", "banana", "orange"}
set2 = {"aeroplane","bus","apple"}
# set3 = set1.union(set2)
# set1.update(set2)
# set3 = set1.intersection(set2)
set1.intersection_update(set2)
# set3 = set1.difference(set2)
# set3 = set1.symmetric_difference(set2)
set1.symmetric_difference_update(set2)
print(set1)
# print(set3)



