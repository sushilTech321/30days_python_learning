import os

# Python File handling

"""
1. File handling is an important part of any web application.

2. Python has several functions for creating, reading, updating, and deleting files.

3. File Handling -> The key function open(), takes two parameters; filename, and mode.

4. four different methods (modes) for opening a file: "r" - Read, "a" - Append, "w" - Write , "x" - Create, "t" - Text , "b" - Binary 

"""

# Syntax
# f = open("demofile","r")   
# print(f.read())
# print(f.read(5))
# print(f.readline())

# using loop
# for x in f:
#     print(x)
# f.close()


# Python File Write
# f = open("demofile","a")   
# f.write("\nAru sunau yr k xa")
# f.close()

# #open and read the file after the appending:
# f = open("demofile","r")   
# print(f.read())

# overriding content of demofile2
# f = open("demofile2","w")   
# f.write("yo text le demofile2 ko content lai overwrite garxa")
# f.close()

# f = open("demofile2","r")   
# print(f.read())


# Create a New File
# f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")


if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

