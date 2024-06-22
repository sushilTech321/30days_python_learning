"""
1.List[] -> chengeable, ordered , and allow duplicate
2. Negative Indexing -> Negative indexing means start from the end
                     -> -1 refers to the last item, -2 refers to the second last item etc.
"""

list1 = ["Apple",12,"banana","Apple","true","false"]
print("displaying the list1: \n",list1)
print("\n")
print ("this is the length of list1:", len(list1))
print("\n")

# using list constructor 
thislist = list(("car","bike","motor","bycle","orange", "kiwi", "melon", "mango"))
print(thislist)

# Access Items
print("Accessing item from the thislist:",thislist[3])

# Negative Indexing
print("Accessing item from the thislist:",thislist[-2])

# Range of Indexes
print("it include index 2 and not include index 5:",thislist[2:5])
print(" it returns item from index 0 and not include index 5:",thislist[:5])

# Range of Negative Indexes

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("it returns the item from -4 i.e. orange but not include mango:",mylist[-4:-1])

# checking if exits in the list

if "watermelon" in mylist:
    print("yes 'watermelon' is in the mylist")
else:
    print("No, 'watermelon', is not in the mylist.")

list2 = ["apple", "banana", "cherry"]
list2[1:2] = ["blackcurrant", "watermelon"]
print(list2)

# Insert Items
name = ["Hari","Shyam", "Radha", "Krishna"]
name.insert(2,"Sita")
print("inserting 'Sita', after Shyam:",name)
print("length of name become:",len(name))

numberList = [1,2,3,4,5]
numberList.insert(3,6)
print(numberList)
