# Python program to interchange first and last elements in a list
# Examples: 
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Approach #1: Find the length of the list and simply swap the first element with (n-1)th element.


def swapList(list1):
    size = len(list1)

    #swapping
    temp = list1[0]
    list1[0] = list1[size - 1]
    list1[size - 1] = temp
    return list1

list1 = [ 12, 35, 9, 56, 24 ]
print(swapList(list1))

# Approach #2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].

def swapList(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1
list1 = [ 12, 35, 9, 56, 24 ]
print(swapList(list1))


"""
Approach #3: Swap the first and last element is using tuple variable.
Store the first and last element as a pair in a tuple variable, say get, 
and unpack those elements with first and last element in that list.
Now, the First and last values in that list are swapped. 

"""

def swapList(list2):
    
    #storing first and last element as a pair in a tuple variable
    get = list2[0], list2[-1]
    
    #unpacking element
    list2[-1], list2[0] = get

    return list2

lists = [ 12, 35, 9, 56, 24 ]
print(swapList(lists))
 
"""
Approach #4: Using * operand. 
This operand proposes a change to iterable unpacking syntax, 
allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name. 
"""

def swapList(list):
    
    start, *middle, end = list
    list = [end, *middle, start]

    return list

lists = [ 12, 35, 9, 56, 24 ]
print(swapList(lists))


"""
Approach #5: Swap the first and last elements is to use the inbuilt function list.pop(). 
Pop the first element and store it in a variable. Similarly, pop the last element and store it in another variable. 
Now insert the two popped element at each other’s original position. 
"""

def swalist5(list5):
    fe = list5.pop(0)
    le = list5.pop(-1)

    list5.insert(0,le)
    list5.append(fe)

    return list5

lists = [ 12, 35, 9, 56, 24 ]
print(swalist5(lists))


# Python | Find elements of a list by indices
"""
Given two lists with elements and indices, write a Python program to find elements of list 1 at indices present in list 2. 

Examples:
Input : lst1 = [10, 20, 30, 40, 50]
    lst2 = [0, 2, 4]
Output : [10, 30, 50]

Explanation: 
Output elements at indices 0, 2 and 4 i.e 10, 30 and 50 respectively. 

Input : lst1 = ['Hello', 'geeks', 'for', 'geeks']
        lst2 = [1, 2, 3]
Output : ['geeks', 'for', 'geeks']

Approach #1 : Naive(List comprehension) The first approach to find the desired elements is to use list comprehension.
We traverse through ‘lst2’ and for each ith element, we output lst1[i]. 

"""
print()
print("")

def findEle(lst1, lst2):
    return [lst1[i] 
            
    for i in lst2]

# lst1 = [10, 20, 30, 40, 50]
# lst2 = [0, 2, 4]

lst1 = ['Hello', 'geeks', 'for', 'geeks']
lst2 = [1, 2, 3]
print(findEle(lst1, lst2))