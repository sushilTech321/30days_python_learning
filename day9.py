# Python Functions -> A function is a block of code which only runs when it is called.
# Creating a Function

# def my_function():
#     print("This is a functon")
# my_function()


# Arguments -> Information can be passed into functions as arguments.
# def my_function(fname):
#     print(fname + " Bahun ")
# my_function("Jack")    
# my_function("James")    
# my_function("Weekend")    
# my_function("Billie")  

# calling function using loop 
# names = ["Jack", "James", "Weekend", "Billie"]  
# for name in names:
#     my_function(name)


# def info(fname, lname):
#     print(fname+" "+lname)
# info("James","Land")
# info("Jack","Bhosadiwale")


#passsing arguments with loop 

# names = [
#     ("James", "Land"),
#     ("Jack", "Bhosadiwale")
# ]

# for fname, lname in names:
#     info(fname,lname)

# names = [
#     {"fname": "James", "lname": "Land"},
#     {"fname": "Jack", "lname": "Bhosadiwale"}
# ]

# for persons in names:
#     info(persons["fname"],persons["lname"])


# Python Lambda -> A lambda function is a small anonymous function

# x = lambda a : a + 10
# x = lambda a, b : a * b
# x = lambda a, b, c : a + b + c
# print(x(5,5,5))

def myfunc(n):
    return lambda a : a * n

doubler = myfunc(2)
tripler = myfunc(3)
fourther = myfunc(13)

print(doubler(11))
print(tripler(10))
print(fourther(10))

